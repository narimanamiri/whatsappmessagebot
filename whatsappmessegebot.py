from twilio.rest import Client

# Set up Twilio client
account_sid = 'YOUR_ACCOUNT_SID_HERE'
auth_token = 'YOUR_AUTH_TOKEN_HERE'
client = Client(account_sid, auth_token)

# Read phone numbers from file
with open('numbers.list', 'r') as f:
    numbers = f.read().splitlines()

# Set message to send
message = 'YOUR_MESSAGE_HERE'

# Loop through phone numbers and send message
for number in numbers:
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=message,
        to=f'whatsapp:{number}'
    )
    print(f'Message sent to {number}: {message.sid}')
