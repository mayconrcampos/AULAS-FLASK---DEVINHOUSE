from flask import Flask
from src.app.controllers.usuarios import usuario

def routes(app: Flask):
    app.register_blueprint(usuario)