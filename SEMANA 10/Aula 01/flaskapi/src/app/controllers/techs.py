from flask import Blueprint, jsonify, request
from src.app.models.tech import technologiesSchema, Tech
from src.app.db import db, ma

technology = Blueprint("technology", __name__, url_prefix="/technology")

@technology.route("/", methods=["GET"])
def get_all_techs():

    tech = Tech.query.all()
    techs_all = technologiesSchema.dump(tech)
    
    return jsonify(techs_all)
    


@technology.route("/", methods=["POST"])
def insert_tech():
    body = request.get_json()

    print(body)

    tech = Tech(
        name=body["name"]
    )

    db.session.add(tech)
    db.session.commit()

    return {
        "mensagem": "Item inserido com sucesso"}, 201