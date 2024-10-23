import ollama

ollama.pull('llama3.1')


def generate_response(message):
    response = ollama.chat(model='llama3.1', messages=[
      {
        'role': 'user',
        'content': message,
      },
    ])
    return response['message']['content']
