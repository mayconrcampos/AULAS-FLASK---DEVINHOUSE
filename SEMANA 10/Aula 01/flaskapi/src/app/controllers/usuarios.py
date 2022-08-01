from flask import Blueprint


usuario = Blueprint("usuario", __name__, url_prefix="/usuario")

@usuario.route("/", methods=["GET"])
def lista_all():
    return "<h1>Olá todos usuários</h1>"