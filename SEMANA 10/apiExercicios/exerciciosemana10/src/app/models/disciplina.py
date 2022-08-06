from src.app.db import db, ma

class Disciplina(db.Model):
    __tablename__ = "disciplinas"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    carga_horaria = db.Column(db.Integer, nullable=False)

    def __init__(self, nome, carga_horaria) -> None:
        self.nome = nome
        self.carga_horaria = carga_horaria
    
class DisciplinaSchema(ma.Schema):
    class Meta:
        fields = ("id", "nome", "carga_horaria")

disciplina_share_schema = DisciplinaSchema()