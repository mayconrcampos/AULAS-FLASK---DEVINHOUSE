from flask import Blueprint, request
from src.app.db import database, Query

usuario = Blueprint("usuario", __name__, url_prefix="/usuario")


@usuario.route("/", methods=["GET"])
def list_all():
    users = database.all()
    if users:
        return {"usuarios": users}, 200
    
    return {"erro": "Nenhum usuario encontrado"}, 404


@usuario.route("/<id>", methods=["GET"])
def list_one_user(id):
    user = database.get(doc_id=id)

    if user:
        return {
            "usuario": user
        }, 200
    
    return {"erro": "usuário não encontrado"}, 404


@usuario.route("/", methods=["POST"])
def insert_user():
    user = request.get_json()
    insert = database.insert(user)

    if insert:
        return {
            "id": insert,
            "mensagem": "usuario inserido com sucesso",
            "usuario": user
            }, 202
    
    return {"erro" "erro ao inserir usuário"}, 403

@usuario.route("/<cpf>", methods=["PATCH"])
def update_user(cpf):
    dados = request.get_json()

    user = Query()
     
    existe = database.search(user.cpf == cpf)

    if existe:
        database.update({
            "nome": dados["nome"],
            "email": dados['email']
        }, user.cpf == cpf)

        return {
            "mensagem": "Usuário atualizado com sucesso",
            "usuario_antigo": existe,
            "usuário_atualizado": dados
        }, 204
    return {"erro": "erro ao atualizar usuário"}, 404


@usuario.route("/<string:id>", methods=["DELETE"])
def delete_user(id: str):
    if id.isnumeric():
        user = database.get(doc_id=id)

        if user:
            database.remove(Query()["nome"] == user["nome"])

            return {
                "mensagem": "Usuário removido com sucesso",
                "usuario": user
            }, 200
        return {
            "erro": "Usuário não encontrado"
        }, 404
    
    return {
        "erro": "id inválido. É preciso ser numérico."
    }