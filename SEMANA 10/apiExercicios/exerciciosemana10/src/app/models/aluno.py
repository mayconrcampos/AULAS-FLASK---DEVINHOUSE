from src.app.db import db, ma 
from src.app.models.curso import Curso

class Aluno(db.Model):
    __tablename__ = "alunos"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    data_entrada = db.Column(db.Date, nullable=False)
    cotista = db.Column(db.Boolean, nullable=False)
    id_curso = db.Column(db.Integer, db.ForeignKey(Curso.id), nullable=False)

    def __init__(self, id, nome, data_entrada, cotista, id_curso):
        self. id = id
        self.nome = nome
        self.data_entrada = data_entrada
        self.cotista = cotista
        self.id_curso = id_curso


class AlunoSchema(ma.Schema):
    class Meta:
        fields = ("id", "nome", "data_entrada", "cotista", "id_curso")


aluno_share_schema = AlunoSchema()

