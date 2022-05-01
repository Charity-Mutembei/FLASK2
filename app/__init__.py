from flask import Flask
from .config import DevConfig

#initializing application
app = Flask(__name__, static_url_path='/app/static')

#setting up configuration
app.config.from_object(DevConfig)

from app import views
