from flask import Flask

from .settings import configure


app = Flask(__name__)

configure(app)
