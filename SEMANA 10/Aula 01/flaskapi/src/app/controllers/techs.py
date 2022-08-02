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


@technology.route("/<int:id>", methods=["GET"])
def get_one_tech(id: int):
    try:
        busca_tech = db.session.query(Tech).filter_by(id=id)
        tech = technologiesSchema.dump(busca_tech)

        if tech:
            return jsonify(tech), 200

        return {
            "erro": "Item não encontrado"
        }, 404
    

    except:
        return {"erro": "ID Inválido"}


@technology.route("/<int:id>", methods=["PATCH"])
def update_tech(id: int):
    body = request.get_json()
    busca_tech = db.session.query(Tech).filter_by(id=id).update(
        {"name": body["name"]}, synchronize_session="fetch"
    )
    
    if busca_tech:
        db.session.commit()
        return {"mensagem": f"item ID: {id} atualizado com sucesso"}, 200
    
    return {
        "erro": "Item não encontrado"
    }, 404


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


@technology.route("/<int:id>", methods=["DELETE"])
def delete_tech(id: int):
    delete_tech = db.session.query(Tech).filter_by(id=id).delete(synchronize_session="fetch")
    
    if delete_tech:
        db.session.commit()
        return {"mensagem": f"item ID: {id} excluido com sucesso"}, 200
    
    return {
        "erro": "Item não encontrado"
    }, 404