from src.app.controllers.alunos import aluno
from src.app.controllers.disciplinas import disciplina

def routes(app):
    app.register_blueprint(aluno)
    app.register_blueprint(disciplina)