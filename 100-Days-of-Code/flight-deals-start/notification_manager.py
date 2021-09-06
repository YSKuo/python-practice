import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

from_number = os.getenv("TWILIO_NUMBER")
to_number = os.getenv("MY_NUMBER")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_ACCOUNT_SID")


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_sms(self, flight_data):
        message = self.client.messages.create(
            body=f"Sent from your Twilio trial account - Low price alert! Only £{flight_data.price} to fly from {flight_data.origin_city}-{flight_data.origin_airport} to {flight_data.destination_city}-{flight_data.destination_airport}, from {flight_data.depart_date} to {flight_data.return_date}",
            from_=from_number,
            to=to_number
        )
        print(message.status)
