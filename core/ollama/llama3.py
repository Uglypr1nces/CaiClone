import os
os.environ["OLLAMA_HOST"] = "http://127.0.0.1:10273"

import ollama
from ollama import Client

client = Client()

client.pull("llama3.1")

def generate_response(message):
    response = client.chat(model='llama3.1', messages=[
        {
            'role': 'user',
            'content': message,
        },
    ])
    return response['message']['content']
