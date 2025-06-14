# Azure AI Vision: OCR Quickstart

This project demonstrates how to use the Azure AI Vision Image Analysis 4.0 SDK in Python to extract text from images using Optical Character Recognition (OCR).

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
- Analyze the specified local image for text
- Print the detected text and confidence scores to the console
- Create an annotated version of the image showing text locations

The script will create a new file with "_ocr" suffix (e.g., `image_ocr.jpg`) containing:
- Blue polygons around lines of text
- Green polygons around individual words
- Text labels in blue above each line

## Example Output

```
OCR analysis results:

Detected text:
Line: 'challenges: building Cursor'
  Word: 'challenges:' (confidence: 87.80%)
  Word: 'building' (confidence: 70.70%)
  Word: 'Cursor' (confidence: 96.50%)

Annotated image saved as: image_ocr.jpg
```

## References

- [Official Microsoft Quickstart Guide](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/quickstarts-sdk/image-analysis-client-library-40?pivots=programming-language-python&tabs=visual-studio%2Clinux)
