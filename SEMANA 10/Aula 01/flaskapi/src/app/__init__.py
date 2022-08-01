from flask import Flask
import os
from src.app.config import app_config
from src.app.routes import routes


app = Flask(__name__)

app.config.from_object(app_config[os.getenv("FLASK_ENV")])
routes(app)

@app.route("/")
def index():
    return "<h1>Olá mundow</h1>"
