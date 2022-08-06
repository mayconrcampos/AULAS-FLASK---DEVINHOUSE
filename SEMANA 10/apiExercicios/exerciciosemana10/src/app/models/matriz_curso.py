from src.app.db import ma, db 
from src.app.models.disciplina import Disciplina
from src.app.models.curso import Curso


class MatrizCurso(db.Model):
    __tablename__ = "matrizes_cursos"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    id_curso = db.Column(db.Integer, db.ForeignKey(Curso.id), nullable=False)
    id_disc = db.Column(db.Integer, db.ForeignKey(Disciplina.id), nullable=False)
    periodo = db.Column(db.Integer, nullable=False)

    def __init__(self, id, id_curso, id_disc, periodo) -> None:
        self.id = id
        self.id_curso = id_curso
        self.id_disc = id_disc
        self.periodo = periodo

class MatrizCursoSchema(ma.Schema):
    class Meta:
        fields = ("id", "id_curso", "id_disc", "periodo")


matriz_curso_share_schema = MatrizCursoSchema()

