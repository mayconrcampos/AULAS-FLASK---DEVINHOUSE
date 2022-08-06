from crypt import methods
from src.app.db import db
from flask import Blueprint, jsonify, request
from src.app.models.disciplina import Disciplina


disciplina = Blueprint("disciplina", __name__, url_prefix="/disciplina")


@disciplina.route("/", methods=["GET"])
def get_all_disciplinas():
    get_all = db.session.query(Disciplina).all()

    if get_all:
        alunos = [{
            "id": disc.id,
            "nome": disc.nome,
            "carga_horaria": disc.carga_horaria
            }
            for disc in get_all]

        return {"data": alunos}, 200
    return {"erro": "Nenhuma disciplina cadastrada"}, 404


@disciplina.route("/", methods=["POST"])
def insert_disciplina():
    body = request.get_json()

    if body["nome"] and body["carga_horaria"]:
        disc = Disciplina(
            nome=body["nome"],
            carga_horaria=body["carga_horaria"]
        )

        db.session.add(disc)
        db.session.commit()

        return {
            "mensagem": "Disciplina inserida com sucesso",
            "disciplina": body
        }, 201
    

    return {
        "erro": "É preciso informas os campos"
    }, 403
