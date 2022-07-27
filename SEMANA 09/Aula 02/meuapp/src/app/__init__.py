from crypt import methods
from flask import Flask
import os
from src.app.config import app_config

app = Flask(__name__)

#Após a execução da variável app
app.config.from_object(app_config[os.getenv('FLASK_ENV')])


@app.route("/", methods=["GET"])
def hello_world():
    return "<h1>Hello Worldcccc</h1>"