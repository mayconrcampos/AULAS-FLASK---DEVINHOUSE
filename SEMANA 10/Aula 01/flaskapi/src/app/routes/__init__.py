from src.app.controllers.techs import technology

def routes(app):
    app.register_blueprint(technology)