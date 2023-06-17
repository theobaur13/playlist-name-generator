from flask import Flask
# from keys import config_key #
from dotenv import load_dotenv
from pathlib import Path
import os
from app.gpt import openai

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("CONFIG_KEY")

openai.api_key = os.getenv("OPENAI_SECRET_KEY")

from app import routes