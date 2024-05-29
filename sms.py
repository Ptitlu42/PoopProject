from twilio.rest import Client

from config import account_sid, auth_token, destination_number

client = Client(account_sid, auth_token)

SENDBY = ""
SMS_BODY = ""

def send_sms(body, to=destination_number, from_=SENDBY):
    msg = client.messages.create(
        body=body,
        from_=from_,
        to=to
    )
    return msg.sid

if __name__ == "__main__":
    sms_body = SMS_BODY
    message_sid = send_sms(sms_body)
    print(f"Sent message with SID: {message_sid}")