import os
from dotenv import load_dotenv
import argparse
from PIL import Image, ImageDraw, ImageFont
import os.path

from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential


def get_vision_client():
    """Initialize and return Azure Vision client."""
    load_dotenv()
    endpoint = os.getenv("VISION_ENDPOINT")
    key = os.getenv("VISION_KEY")
    return ImageAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))


def read_image(image_path):
    """Read image file and return its binary data."""
    with open(image_path, "rb") as image_file:
        return image_file.read()


def analyze_image(client, image_data):
    """Analyze image using Azure Vision client."""
    return client.analyze(
        image_data=image_data,
        visual_features=[
            VisualFeatures.CAPTION,
            VisualFeatures.TAGS,
            VisualFeatures.OBJECTS,
            VisualFeatures.PEOPLE,
        ],
        gender_neutral_caption=True,
    )


def print_caption(result):
    if result.caption is not None:
        print("\nCaption:")
        print(
            " Caption: '{}' (confidence: {:.2f}%)".format(
                result.caption.text, result.caption.confidence * 100
            )
        )

    if result.dense_captions is not None:
        print("\nDense Captions:")
        for caption in result.dense_captions.list:
            print(
                " Caption: '{}' (confidence: {:.2f}%)".format(
                    caption.text, caption.confidence * 100
                )
            )


def print_tags(result):
    """Print tags analysis results."""
    print("Tags:")
    if result.tags is not None:
        for tag in result.tags.list:
            print(" Tag: '{}' (confidence: {:.2f}%)".format(tag.name, tag.confidence * 100))


def get_font(size=18):
    try:
        return ImageFont.truetype("Arial", size)
    except IOError:
        return ImageFont.load_default()


def annotate_objects(image_path, objects):
    """Create an annotated copy of the image with detected objects highlighted."""
    original_image = Image.open(image_path)
    annotated_image = original_image.copy()
    draw = ImageDraw.Draw(annotated_image)

    font = get_font()
    
    for obj in objects:
        box = obj.bounding_box
        x = int(box.x)
        y = int(box.y)
        width = int(box.width)
        height = int(box.height)

        draw.rectangle(
            [(x, y), (x + width, y + height)],
            outline="red",
            width=3
        )

        draw.text(
            (x, y - 40),
            obj.tags[0].name,
            fill="red",
            font=font
        )
    
    # Create output filename
    base, ext = os.path.splitext(image_path)
    output_path = f"{base}_annotated{ext}"
    
    # Save the annotated image
    annotated_image.save(output_path)
    print(f"\nAnnotated image saved as: {output_path}")


def print_objects(result, image_path):
    """Print and visualize detected objects in the image."""
    print("\nObjects in image:")
    for detected_object in result.objects.list:
        # Print object tag and confidence
        print(" {} (confidence: {:.2f}%)".format(
            detected_object.tags[0].name,
            detected_object.tags[0].confidence * 100
        ))
    # Create annotated version of the image
    annotate_objects(image_path, result.objects.list)


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Analyze an image using Azure Computer Vision"
    )
    parser.add_argument("image_path", help="Path to the image file to analyze")
    return parser.parse_args()


def main():
    """Main function to orchestrate the image analysis process."""
    args = parse_args()
    client = get_vision_client()
    image_data = read_image(args.image_path)
    result = analyze_image(client, image_data)
    
    print("Image analysis results:")
    print_caption(result)
    print_tags(result)
    print_objects(result, args.image_path)


if __name__ == "__main__":
    main()
