from flask import Blueprint, jsonify
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

    return {"data": todos}