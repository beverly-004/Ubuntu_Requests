import os
import requests
from urllib.parse import urlparse
from datetime import datetime

def fetch_image():
    url = input(" Enter the image URL: ").strip()

    # Create directory if it doesn't exist
    folder_name = "Fetched_Images"
    os.makedirs(folder_name, exist_ok=True)

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses

        # Extract filename from URL or generate one
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        if not filename or '.' not in filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"image_{timestamp}.jpg"

        # Save image in binary mode
        image_path = os.path.join(folder_name, filename)
        with open(image_path, "wb") as f:
            f.write(response.content)

        print(f" Image saved successfully as '{filename}' in '{folder_name}'.")

    except requests.exceptions.RequestException as e:
        print(f"Unable to fetch image. Reason: {e}")

if __name__ == "__main__":
    print(" Ubuntu Image Fetcher: I am because we are.")
    fetch_image()