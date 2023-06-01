import base64
from twilio.rest import Client

def hello_pubsub(event, context):
    if 'data' in event:
        try:
            # Retrieve the data from the event payload
            data = base64.b64decode(event['data']).decode('utf-8')
            data_dict = eval(data)  # Convert the data string to a dictionary
            longitude = data_dict.get('longitude')
            latitude = data_dict.get('latitude')

            # Generate the Google Maps link
            maps_url = f"https://www.google.com/maps?q={latitude},{longitude}"

            # Send a message using Twilio
            account_sid = ""
            auth_token = ""
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                to="",
                from_="",
                body=f"Alarm triggered! Please check your device! Location: {maps_url}")

            # Log the result
            print(f"Message sent: {message.sid}")

        except Exception as e:
            print(f"Failed to send message: {str(e)}")
    else:
        print('No data in pub/sub message')