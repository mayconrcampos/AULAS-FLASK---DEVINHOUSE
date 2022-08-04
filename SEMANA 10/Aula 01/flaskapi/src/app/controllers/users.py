from flask import Blueprint, jsonify, request
from src.app.models.user import User, UserSchema
from src.app.db import db, ma
import requests


user = Blueprint("user", __name__, url_prefix="/user")


@user.route("/<int:qtde>", methods=["GET"])
def get_all(qtde: int):
    data = requests.get(f"https://randomuser.me/api/?nat=br&results={qtde}")

    for coisa in data.json()['results']:
        nomeCompleto = f"{coisa['name']['first']} {coisa['name']['last']}"
        age = coisa['dob']['age']
        email = coisa['email']
        password = coisa["login"]["username"]

        print(nomeCompleto, age, email, password)    

        
    return jsonify(data.json()["results"])
