def get_prompt(message, character_name, character_description):
    prompt = f"Stay fully in character as {character_name}, described as {character_description}. Respond to the following message in character: {message}. Do not break character, provide out-of-character commentary, or speak on behalf of the user."
    return prompt