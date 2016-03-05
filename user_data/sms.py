from twilio.rest import TwilioRestClient
import os

SMS_PHONE = os.getenv('RESPONDERS_PHONE')
SMS_TWILIO_ACCOUNT_SID = os.getenv('RESPONDERS_TWILIO_ACCOUNT_SID')
SMS_AUTH_TOKEN = os.getenv('RESPONDERS_AUTH_TOKEN')
client = TwilioRestClient(SMS_TWILIO_ACCOUNT_SID, SMS_AUTH_TOKEN)

def send_message_to(phone_number, message):
    message = client.messages.create(body=message,
        to="+{}".format(phone_number),
        from_="+{}".format(SMS_PHONE)
        )
    # must start with country code (1) 
    return 'ok, I sent a message (sid {message.sid}) to {phone_number} saying {message}'.format(**locals())
