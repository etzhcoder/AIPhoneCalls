import os
import sys
import openai
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv



_ = load_dotenv(find_dotenv())
client = OpenAI(
    api_key = os.getenv("APIKEY")
)

def get_user_input(prompt="You: "):
    return input(prompt)

def generate_response(input, model="tts-1", voice="alloy"):
    try:
        response = client.audio.speech.create(
            model = model,
            voice = voice,
            input = input
        )
        return response.with_streaming_response.method("output.mp3")
    except openai.OpenAIError as e:
        return f"Error: {str(e)}"