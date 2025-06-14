import os
from dotenv import load_dotenv
import argparse
from PIL import Image, ImageDraw, ImageFont

from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential


def get_font(size=18):
    """Get a font with specified size, falling back to default if Arial is not available."""
    try:
        return ImageFont.truetype("Arial", size)
    except IOError:
        return ImageFont.load_default()


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
    """Analyze image using Azure Vision client for OCR."""
    return client.analyze(
        image_data=image_data,
        visual_features=[VisualFeatures.READ],
    )


def annotate_text(image_path, result):
    """Create an annotated copy of the image with detected text highlighted."""
    original_image = Image.open(image_path)
    annotated_image = original_image.copy()
    draw = ImageDraw.Draw(annotated_image)
    font = get_font()

    if result.read is not None:
        for block in result.read.blocks:
            for line in block.lines:
                # Draw bounding box for each line
                points = line.bounding_polygon
                if len(points) >= 4:  # Ensure we have enough points for a polygon
                    # Convert points to list of tuples
                    polygon_points = [(point.x, point.y) for point in points]
                    draw.polygon(polygon_points, outline="blue", width=2)
                
                    # Draw text above the line
                    x, y = polygon_points[0]  # Use first point as reference
                    draw.text(
                        (x, y - 20),
                        line.text,
                        fill="blue",
                        font=font
                    )

                # Draw bounding boxes for individual words
                for word in line.words:
                    word_points = word.bounding_polygon
                    if len(word_points) >= 4:
                        # Convert word points to list of tuples
                        word_polygon = [(point.x, point.y) for point in word_points]
                        draw.polygon(word_polygon, outline="green", width=1)
    
    # Create output filename
    base, ext = os.path.splitext(image_path)
    output_path = f"{base}_ocr{ext}"
    
    # Save the annotated image
    annotated_image.save(output_path)
    print(f"\nAnnotated image saved as: {output_path}")


def print_ocr_results(result):
    """Print OCR analysis results."""
    if result.read is not None:
        print("\nDetected text:")
        for block in result.read.blocks:
            for line in block.lines:
                print(f"Line: '{line.text}'")
                for word in line.words:
                    print(f"  Word: '{word.text}' (confidence: {word.confidence:.2%})")


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Extract text from an image using Azure Computer Vision OCR"
    )
    parser.add_argument("image_path", help="Path to the image file to analyze")
    return parser.parse_args()


def main():
    """Main function to orchestrate the OCR process."""
    args = parse_args()
    client = get_vision_client()
    image_data = read_image(args.image_path)
    result = analyze_image(client, image_data)
    
    print("OCR analysis results:")
    print_ocr_results(result)
    annotate_text(args.image_path, result)


if __name__ == "__main__":
    main()
