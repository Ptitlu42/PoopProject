from openai import OpenAI
from random_messages import generate_random_message
from config import openai_key


def generate_image():
    client = OpenAI(api_key=openai_key)

    response = client.images.generate(
    model="dall-e-3",
    prompt=generate_random_message(),
    size="1024x1024",
    quality="hd",
    n=1,
    )

    return response.data[0].url
