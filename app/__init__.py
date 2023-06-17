from flask import Flask
# from keys import config_key #
from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("CONFIG_KEY")

from app import routes