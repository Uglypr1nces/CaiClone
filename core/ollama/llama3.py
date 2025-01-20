import os
os.environ["OLLAMA_HOST"] = "http://127.0.0.1:10273"

import ollama
from ollama import Client

client = Client()

client.pull("llama2-uncensored")

def generate_response(message):
    response = client.chat(model='llama2-uncensored', messages=[
        {
            'role': 'user',
            'content': message,
        },
    ])
    return response['message']['content']
