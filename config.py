import os
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_number = os.getenv('TWILIO_PHONE_NUMBER')
destination_number = os.getenv('DESTINATION_PHONE_NUMBER')
phone_number_sid = os.getenv('PHONE_NUMBER_SID')
openai_key = os.getenv('OPEN_API_KEY')
