import openai
from keys import openai_secret_key

openai.api_key = openai_secret_key

def generate_playlist_name(playlist_info):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Create a playlist name for the following playlist:\n\n" + str(playlist_info) + "\n\nPlaylist name:",
        max_tokens=10
    )
    playlist_name = response["choices"][0]["text"]
    return playlist_name