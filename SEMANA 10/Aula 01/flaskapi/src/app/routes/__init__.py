from src.app.controllers.techs import technology
from src.app.controllers.users import user
from src.app.controllers.countries import country

def routes(app):
    app.register_blueprint(technology)
    app.register_blueprint(user)
    app.register_blueprint(country)
    