from generate_image import generate_image
from sms import send_sms
from random_messages import generate_random_message
from config import openai_key, destination_number, destination_number2
from image_download import download_image
from drive import drive_image

message = generate_random_message()
prompt = f"{message} with a big POOP"
image_url = generate_image(prompt)
image_path = download_image(image_url)
dl_link = drive_image(f"generated/{image_path}")
daily_message = f" \n {message}\n \n \n \n  C'est ton CACA du jour, tu veux le découvrir? \n \n \n {dl_link}"
send_sms(message=daily_message, destination_number=destination_number)
send_sms(message=daily_message, destination_number=destination_number2)

print ("Poop finished.")
