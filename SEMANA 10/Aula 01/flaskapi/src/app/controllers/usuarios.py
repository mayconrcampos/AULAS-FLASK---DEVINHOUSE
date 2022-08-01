from flask import Blueprint
from src.app.models import tech


technology = Blueprint("technology", __name__, url_prefix="/technology")

@technology.route("/", methods=["GET"])
def lista_all():
    return "<h1>Olá todos usuários</h1>"