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

Run the main script:

```sh
python image-analysis-quickstart/main.py
```

This will:
- Connect to Azure AI Vision using your credentials
- Analyze a sample image from a URL
- Print the generated caption and any detected text (OCR) to the console

## Example Output

```
Endpoint: https://<your-resource-name>.cognitiveservices.azure.com/
Key: <your-key>
Image analysis results:
Caption:
   'A group of people standing in a room', Confidence 0.9876
Read:
   Line: 'Welcome to the event', Bounding box [...]
     Word: 'Welcome', Bounding polygon [...], Confidence 0.98
     Word: 'to', Bounding polygon [...], Confidence 0.99
     Word: 'the', Bounding polygon [...], Confidence 0.97
     Word: 'event', Bounding polygon [...], Confidence 0.96
```

## References

- [Official Microsoft Quickstart Guide](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/quickstarts-sdk/image-analysis-client-library-40?pivots=programming-language-python&tabs=visual-studio%2Clinux)
