from crypt import methods
from flask import Blueprint, request

technology = Blueprint("technology", __name__, url_prefix="/technology")

data = ["Java", "Javascript", "Python"]

@technology.route("/", methods=["GET"])
def list_all_technologies():

    return {
        "data": data
    }

@technology.route("/<int:id_tech>", methods=["GET"])
def list_one_technology(id_tech):


    for _ in range(len(data)):
        if _ == id_tech:
            return {
                "data": data[_]
            }
    
    return {
        "mensagem": f"ID {id_tech} não encontrado." 
    }, 404

    

@technology.route("/", methods=["POST"])
def insert_technologies():
    tech = request.get_json()

    data.append(tech['data'])

    return {
        "mensagem": "Dado inserido com sucesso"
    }

@technology.route("/", methods=["DELETE"])
def pop_item():
    if len(data) > 0:
        dado = data[-1]
        data.pop()

        return {
            "mensagem": f"{dado} excluido com sucesso"
        }
    return {
        "mensagem": "Lista vazia"
    }, 404

    

    
