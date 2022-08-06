from flask import Blueprint

teste = Blueprint("teste", __name__, url_prefix="/teste")

@teste.route("/", methods=['GET'])
def list_all_technologies():
    return {"data": ["Java", "Javascript", "Python"]}