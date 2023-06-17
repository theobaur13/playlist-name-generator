import openai
# from keys import openai_secret_key
from app import os
from dotenv import load_dotenv

openai.api_key = os.getenv("OPENAI_SECRET_KEY")

def generate_playlist_name(playlist_info):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Create a playlist name for the following playlist:\n\n" + str(playlist_info) + "\n\nPlaylist name:",
        max_tokens=10,
        temperature=1.0,
    )
    playlist_name = response["choices"][0]["text"]
    return playlist_name