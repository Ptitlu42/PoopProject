from twilio.rest import Client
from random_messages import generate_random_message
from config import account_sid, auth_token, destination_number

client = Client(account_sid, auth_token)

SENDBY = "Daily POOP"
SMS_BODY = generate_random_message()

def send_sms(body, to=destination_number, from_=SENDBY):
    msg = client.messages.create(
        body=body,
        from_=from_,
        to=to
    )
    return msg.sid

send_sms(SMS_BODY)
