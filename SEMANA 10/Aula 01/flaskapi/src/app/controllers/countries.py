from flask import Blueprint, jsonify, request
from src.app.models.country import Country, countries_share_schema
from src.app.db import db, ma
import requests


country = Blueprint("country", __name__, url_prefix="/country")


@country.route("/", methods=["GET"])
def get_all_countries():
    paises = db.session.query(Country).all()
    #todos_paises = countries_share_schema.dump(paises)

    all_countries = []
    for p in paises:
        all_countries.append({"id": p.id, "name": p.name, "language": p.language})
    return jsonify(all_countries), 200

    return {"erro": "Nenhum pais cadastrado"}, 404