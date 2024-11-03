def get_prompt(message, character_name, character_description):
    prompt = f"this is a roleplay, act as {character_name} and {character_description}. thats the user message: {message}"
    print(prompt)
    return prompt