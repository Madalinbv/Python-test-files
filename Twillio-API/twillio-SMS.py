from twilio.rest import Client
from credentials import account_sid, auth_token, my_cell, my_twilio

# Find these values at https://twilio.com/user/account
client = Client(account_sid, auth_token)

my_msg = "Your message goes here..."

message = client.messages \
    .create(
    body=my_msg,
    from_=my_twilio,
    to=my_cell
)

print(message.sid)