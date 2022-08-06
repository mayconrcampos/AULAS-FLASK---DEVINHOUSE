from os import stat
from src.app.db import db, ma
from src.app.models.disciplina import Disciplina
from src.app.models.aluno import Aluno

class Matricula(db.Model):
    __tablename__ = "matriculas"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nota = db.Column(db.Float, nullable=True)
    faltas = db.Column(db.Integer, nullable=True)
    status = db.Column(db.String, nullable=True)
    semestre = db.Column(db.Integer, nullable=False)
    id_disc = db.Column(db.Integer, db.ForeignKey(Disciplina.id), nullable=False)
    id_aluno = db.Column(db.Integer, db.ForeignKey(Aluno.id), nullable=False)

    def __init__(self, id, nota, faltas, status, id_disc, id_aluno) -> None:
        self.id = id
        self.nota = nota
        self.faltas = faltas
        self.status = status
        self.id_disc = id_disc
        self.id_aluno = id_aluno

class MatriculaSchema(ma.Schema):
    class Meta:
        fields = ("id", "nota", "faltas", "status", "id_disc", "id_aluno")

matricula_share_schema = MatriculaSchema()

