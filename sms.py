from twilio.rest import Client
from random_messages import generate_random_message
from config import account_sid, auth_token

client = Client(account_sid, auth_token)


def send_sms(message, destination_number):
    msg = client.messages.create(
        body=message,
        from_="Daily POOP",
        to=destination_number,
    )
    return msg.sid
