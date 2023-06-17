from flask import Flask
from keys import config_key, openai_secret_key
# import os
from app.gpt import openai

app = Flask(__name__)
# app.config["SECRET_KEY"] = os.environ.get("CONFIG_KEY")
app.config["SECRET_KEY"] = config_key

# openai.api_key = os.environ.get("OPENAI_SECRET_KEY")
openai.api_key = openai_secret_key

from app import routes