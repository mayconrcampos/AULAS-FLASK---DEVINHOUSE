from src.app.db import ma, db

class Departamento(db.Model):
    __tablename__ = "departamentos"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String, nullable=False)

    def __init__(self, id, nome) -> None:
        self.id = id
        self.nome = nome

class DepartamentoSchema(ma.Schema):
    class Meta:
        fields = ("id", "nome")

depto_share_schema = DepartamentoSchema()