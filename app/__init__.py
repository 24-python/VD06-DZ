from flask import Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

from app import routes
