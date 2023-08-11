<p align="center">
    <img src="https://raw.githubusercontent.com/theobaur13/playlist-name-generator/master/app/static/img/AI-Playlist-Name-Gen-Icon.png" alt="logo" width="100" height="100">
</p>

# playlist-name-generator
A Flask-based website that enables users to upload their Apple Music playlists and generate playlist names using GPT-3.5. The Spotify API is used to connect to the user's account and retrieve both their playlists and the songs inside each playlist. The OpenAI API text-davinci-003 model is used to generate names for the playlists based on the songs inside them. 

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

Create a file named **keys.py** into the **playlist-name-generator** directory and add API keys from [Apple Music API](https://developer.apple.com/documentation/applemusicapi), [OpenAI API](https://openai.com/blog/openai-api), and your own custom generated Flask secret key.

```python
config_key = "CUSTOM_CONFIG_KEY"
apple_team_id = "APPLE_TEAM_ID"
apple_key_id = "APPLE_KEY_ID"
apple_secret_key = "-----BEGIN PRIVATE KEY-----APPLE_PRIVATE_KEY-----END PRIVATE KEY-----"
```

Add the environment variables **DEVELOPER_KEY** and **EXPIRY**, these will be overwritten so it doesn't matter what these are set to

```cmd
set DEVELOPER_TOKEN=abcs
set EXPIRY=0
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
