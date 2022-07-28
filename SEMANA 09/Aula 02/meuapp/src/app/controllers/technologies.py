from flask import Blueprint, request

technology = Blueprint("technology", __name__, url_prefix="/technology")

data = ["Java", "Javascript", "Python"]

@technology.route("/", methods=["GET"])
def list_all_technologies():

    return {
        "data": data
    }

@technology.route("/", methods=["POST"])
def insert_technologies():
    tech = request.get_json()

    data.append(tech['data'])

    return {
        "mensagem": "Dado inserido com sucesso"
    }
