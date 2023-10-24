# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from get_content import media_files
import time


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
client = Client(account_sid, auth_token)

twilio_no = os.environ.get("SENDER")
receiver_no = os.environ.get("RECEIVER")

message = client.messages \
    .create(
         body='This was a soppy intro message I wrote. Write you own soppy message here!',
         from_=twilio_no,
         to=receiver_no
     )
print(message.sid)
for dog_pic in media_files:
    message = client.messages \
        .create(
             from_=twilio_no,
             media_url=dog_pic,
             to=receiver_no
         )
    time.sleep(3600)

    print(message.sid)
