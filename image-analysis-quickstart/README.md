# Azure AI Vision: Image Analysis 4.0 Quickstart

This project demonstrates how to use the Azure AI Vision Image Analysis 4.0 SDK in Python to analyze an image, generate a caption, and extract text (OCR).

## Prerequisites

- Python 3.8+
- An Azure subscription
- An Azure AI Vision (Computer Vision) resource ([create one here](https://portal.azure.com/))
- The resource's endpoint and key

## Setup

1. **Clone this repository and install dependencies:**

   ```sh
   uv pip install -r requirements.txt
   ```

2. **Set up your environment variables:**

   Copy the template and fill in your Azure Vision credentials:

   ```sh
   cp .env.template .env
   # Then edit .env to add your VISION_ENDPOINT and VISION_KEY
   ```

## Usage

Run the main script with a local image path:

```sh
python main.py path/to/your/image.jpg
```

This will:
- Connect to Azure AI Vision using your credentials
- Analyze the specified local image
- Print the generated caption and detected objects to the console
- Create an annotated version of the image with bounding boxes and labels

The script will create a new file with "_annotated" suffix (e.g., `image_annotated.jpg`) containing the visualization of detected objects.

## Example Output

```
Image analysis results:

Caption:
 Caption: 'A group of people standing in a room' (confidence: 98.76%)

Objects in image:
 person (confidence: 92.50%)
 person (confidence: 88.50%)
 person (confidence: 76.30%)

Annotated image saved as: image_annotated.jpg
```

## References

- [Official Microsoft Quickstart Guide](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/quickstarts-sdk/image-analysis-client-library-40?pivots=programming-language-python&tabs=visual-studio%2Clinux)
