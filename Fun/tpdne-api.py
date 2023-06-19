import os
import requests
import string
import random
from PIL import Image

def generate_random_filename(length=10, extension='jpg'):
    letters = string.ascii_lowercase
    random_name = ''.join(random.choice(letters) for _ in range(length))
    return f"{random_name}.{extension}"

def save_image_from_url(url, save_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Image saved successfully at {save_path}")
    else:
        print("Failed to download the image.")

def retrieve_and_save_image():
    try:
        response = requests.get('https://thispersondoesnotexist.com/', stream=True)
        if response.status_code == 200:
            random_filename = generate_random_filename()
            save_path = os.path.join(os.getcwd(), random_filename)
            image = Image.open(response.raw)
            image.save(save_path, 'JPEG')
            print(f"Image saved successfully at {save_path}")
        else:
            print("Failed to retrieve the image.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {str(e)}")

# Example usage
retrieve_and_save_image()
