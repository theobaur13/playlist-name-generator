# playlist-name-generator
A Flask-based website that enables users to upload their Spotify playlists and generate playlist names using GPT-3.5. The Spotify API is used to connect to the user's account and retrieve both their playlists and the songs inside each playlist. The OpenAI API text-davinci-003 model is used to generate names for the playlists based on the songs inside them. 

## Installation
Clone repository

```bash
git clone https://github.com/theobaur13/playlist-name-generator
```
Set up virtual environment

```python
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Create a file named **keys.py** into the **playlist-name-generator** directory and add API keys from [Spotify API](https://developer.spotify.com/documentation/web-api), [OpenAI API](https://openai.com/blog/openai-api), and your own custom generated Flask secret key.

```python
config_key = "CUSTOM_CONFIG_KEY"
spotify_client_id = "SPOTIFY_CLIENT_ID"
spotify_client_secret = "SPOTIFY_CLIENT_SECRET"
openai_secret_key = "OPENAI_SECRET_KEY"
```

## Usage

```python
venv\Scripts\activate

# launches website to localhost
py wsgi.py
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
