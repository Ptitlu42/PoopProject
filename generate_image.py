from openai import OpenAI
from config import openai_key

def generate_image(ai_prompt):
    client = OpenAI(api_key=openai_key)

    response = client.images.generate(
        model="dall-e-3",
        prompt=ai_prompt,
        size="1024x1024",
        quality="hd",
        n=1,
    )

    return response.data[0].url