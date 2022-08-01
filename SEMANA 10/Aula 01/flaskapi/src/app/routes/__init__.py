from src.app.controllers.usuarios import usuario

def routes(app):
    app.register_blueprint(usuario)