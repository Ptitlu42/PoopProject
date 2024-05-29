from generate_image import generate_image
from sms import send_sms
from random_messages import generate_random_message
from config import openai_key, destination_number
from image_download import download_image
from drive import drive_image

message = generate_random_message()
print (f"Basic message: {message}")

prompt = f"{message} with a big POOP"
print (f"AI prompt: {prompt}")

image_url = generate_image(prompt)
print (f"Image URL: {image_url}")

image_path = download_image(image_url)
print ("Downloaded image")

dl_link = drive_image(f"generated/{image_path}")
print ("Uploaded image")

daily_message = f"Here's your daily poop! You want to see {message} ? -> {dl_link}"
send_sms(message=daily_message, destination_number=destination_number)
print ("Sent SMS")
