import requests
import sys
import os
import re

project_root = os.path.join(os.path.dirname(__file__), '..', '..')
sys.path.append(project_root)

from openai import OpenAI
from config import openai_key

def generate_image(ai_prompt):

    prompt = "Génère une image de ' " + ai_prompt + " 'style minimaliste, l'élement central de l'image est le caca"
    client = OpenAI(api_key=openai_key)

    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        quality="standard",
        n=1,
    )

    image_url = response.data[0].url

    image_data = requests.get(image_url).content

    safe_filename = slugify(ai_prompt)
    safe_filename = safe_filename + ".png"

    file_path = os.path.join("generated", safe_filename)

    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))

    with open(file_path, 'wb') as f:
        f.write(image_data)

    path_to_return = slugify(ai_prompt)
    path_to_return = path_to_return + ".png"
    return path_to_return


def slugify(text):
        text = text.replace(' ', '_').lower()
        text = re.sub(r'[^\w-]', '', text)
        text = re.sub(r'_{2,}', '_', text)
        return text