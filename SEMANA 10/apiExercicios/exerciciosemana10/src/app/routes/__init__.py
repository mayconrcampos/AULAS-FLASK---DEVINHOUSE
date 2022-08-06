from src.app.controllers.teste import teste

def routes(app):
    app.register_blueprint(teste)