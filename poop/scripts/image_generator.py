import requests
import sys
import os

project_root = os.path.join(os.path.dirname(__file__), '..', '..')
sys.path.append(project_root)

from openai import OpenAI
from config import openai_key

def generate_image(ai_prompt):

    prompt = "Generate an image of ' " + ai_prompt + " 'dans un style minimaliste et mignon, le CACA doit être l'élément principal de l'image"
    client = OpenAI(api_key=openai_key)

    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
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

    print (f"Image " + ai_prompt + " saved to: " + file_path)
    return file_path