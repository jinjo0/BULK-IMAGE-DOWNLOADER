import os
import requests
from tqdm import tqdm

# Define the filename
filename = 'images.txt'

# Create a directory for downloaded images
os.makedirs('downloaded_images', exist_ok=True)

# Read the file and get all URLs
with open(filename, 'r') as file:
    urls = [url.strip() for url in file.readlines() if url.strip()]

# Download images with a progress bar
for url in tqdm(urls, desc='Downloading Images', unit='image'):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses

        # Get the image name from the URL
        image_name = os.path.join('downloaded_images', os.path.basename(url))

        # Write the image to a file
        with open(image_name, 'wb') as img_file:
            img_file.write(response.content)

    except Exception as e:
        print(f"Failed to download {url}: {e}")
