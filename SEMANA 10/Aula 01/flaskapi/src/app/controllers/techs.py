from flask import Blueprint, jsonify, request
from src.app.models.tech import technologiesSchema, Tech
from src.app.db import db, ma

technology = Blueprint("technology", __name__, url_prefix="/technology")

@technology.route("/", methods=["GET"])
def get_all_techs():

    tech = Tech.query.all()
    techs_all = technologiesSchema.dump(tech)

    if techs_all:
        return jsonify(techs_all), 200
    
    return {"erro": "Nenhum item cadastrado"}, 404
    


@technology.route("/", methods=["POST"])
def insert_tech():
    body = request.get_json()

    if body['name']:
        tech = Tech(
            name=body["name"]
        )

        db.session.add(tech)
        db.session.commit()

        return {
            "mensagem": "Item inserido com sucesso",
            "tech": body
            }, 201
    return {
        "erro": "É preciso informar a tecnologia",
        
    }, 403