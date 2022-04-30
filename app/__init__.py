from flask import Flask

#initializing application
app = Flask(__name__, static_url_path='/app/static')

from app import views
