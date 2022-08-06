from src.app.db import ma, db
from src.app.models.departamento import Departamento

class Curso(db.Model):
    __tablename__ = "cursos"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    id_depto = db.Column(db.Integer, db.ForeignKey(Departamento.id), nullable=False)

    def __init__(self, id, nome, id_depto) -> None:
        self.id = id
        self.nome = nome
        self.id_depto = id_depto

class CursoSchema(ma.Schema):
    class Meta:
        fields = ("id", "nome", "id_depto")


curso_share_schema = CursoSchema()