from flask import Flask
import os
from src.app.config import app_config
from src.app.routes import routes

from src.app.db import db, ma
from src.app.config import app_config
from src.app.routes import routes
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)

    app.config.from_object(app_config[os.getenv("FLASK_ENV")])
    db.init_app(app)
    ma.init_app(app)
    routes(app)

    from src.app.models import tech, devs, country, state, city, user, developers_tech

    Migrate(app=app, db=db, directory="./src/app/migrations")

    return app
