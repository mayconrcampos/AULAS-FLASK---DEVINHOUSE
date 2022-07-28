from flask import Flask
from src.app.controllers.technologies import technology
from src.app.controllers.developers import developers

def routes(app: Flask):
    app.register_blueprint(technology)
    app.register_blueprint(developers)