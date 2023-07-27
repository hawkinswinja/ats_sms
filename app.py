#!/usr/bin/env python3
"""ussd module service
"""
from flask import Flask, request
from sendSMS import SMS


app = Flask(__name__)


@app.route('/test')
def hello():
    """checks if service is running"""
    return '', 200


@app.route('/sms', methods=['POST'])
def main():
    """Main entry point for sms service"""
    content: list = request.get_json()
    message: str = content.get('message')
    recipients = content.get('recipients')
    print(recipients, message)
    count = 0
    try:
        response = SMS().send(recipients, message)['SMSMessageData']
        for user in response['Recipients']:
            if user['status'] == 'Success':
                count += 1
    except Exception:
        pass
    return {'count': count}
    # testing return ', '.join(recipients) + '\n' + message
