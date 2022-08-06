from flask import Blueprint, jsonify, request
from src.app.models.aluno import Aluno
from src.app.db import db

aluno = Blueprint("aluno", __name__, url_prefix="/aluno")

@aluno.route("/", methods=['GET'])
def list_all_alunos():

    all_alunos = db.session.query(Aluno).all()

    todos = [{
            "nome": aluno.nome,
            "data_entrada": aluno.data_entrada,
            "cotista": aluno.cotista,
            "id_curso": aluno.id_curso
            } for aluno in all_alunos]
    if todos:
        return {"data": todos}, 200
    return {"erro": "Nenhum aluno cadastrado"}


@aluno.route("/<int:id>", methods=["PATCH"])
def update_aluno(id):
    body = request.get_json()

    busca_aluno = db.session.query(Aluno).filter_by(id=id).update(
        {
            "nome": body["nome"],
            "cotista": body["cotista"]
        }
    )

    if busca_aluno:
        db.session.commit()
        return {"mensagem": f"Aluno com id {id} atualizado com sucesso"}, 200
    return {"erro": f"Aluno com id {id} não encontrado."}