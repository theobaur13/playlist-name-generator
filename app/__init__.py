from flask import Flask
from keys import config_key, openai_secret_key
from app.gpt import openai

app = Flask(__name__)
app.config["SECRET_KEY"] = config_key

from app import routes