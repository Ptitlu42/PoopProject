import requests
import sys
import os

project_root = os.path.join(os.path.dirname(__file__), '..', '..')
sys.path.append(project_root)

from openai import OpenAI
from config import openai_key

def generate_image(ai_prompt):
    client = OpenAI(api_key=openai_key)

    response = client.images.generate(
        model="dall-e-3",
        prompt=ai_prompt,
        size="512x512",
        quality="standard",
        n=1,
    )

    image_url = response.data[0].url

    image_data = requests.get(image_url).content

    safe_filename = "".join(char for char in ai_prompt if char.isalnum() or char in (" ", "_")).rstrip()

    file_path = os.path.join("generated", safe_filename + ".png")

    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))

    with open(file_path, 'wb') as f:
        f.write(image_data)

    return file_path