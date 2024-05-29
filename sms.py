import os
from twilio.rest import Client

from config import account_sid, auth_token, twilio_number, destination_number

client = Client(account_sid, auth_token)

sendby=""
message=""

def send_sms(body, to=destination_number, from_=sendby):
    message = client.messages.create(
        body=body,
        from_=from_,
        to=to
    )
    return message.sid

if __name__ == "__main__":
    sms_body = message
    message_sid = send_sms(sms_body)

