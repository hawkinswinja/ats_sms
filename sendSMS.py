# works with both python 2 and 3
from __future__ import print_function

import africastalking
from os import getenv


class SMS:
    def __init__(self):
        # get app credentials for authorization
        self.username = getenv('user')  # username in Africastalking app
        self.api_key = getenv('AK')  # APIKEY

        # Initialize the SDK
        africastalking.initialize(self.username, self.api_key)

        # Get the SMS service
        self.sms = africastalking.SMS

    def send(self, recipients: list, message: str) -> str:
        # Set your shortCode or senderId
        # sender = "XXYYZZ"
        try:
            # send message
            response = self.sms.send(message, recipients)
            return response
        except Exception as e:
            return str(e)
