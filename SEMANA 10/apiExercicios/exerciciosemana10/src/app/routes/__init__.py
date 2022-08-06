from src.app.controllers.alunos import aluno

def routes(app):
    app.register_blueprint(aluno)