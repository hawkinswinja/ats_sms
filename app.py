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
    if recipients:
        return SMS().send(recipients, message)
        # testing return ', '.join(recipients) + '\n' + message
    return message, 404
