from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse
import requests

app = Flask(__name__)

@app.route("/twilio/voice", methods=['POST'])
def handle_call():
    response = VoiceResponse()