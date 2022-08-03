from src.app.db import db, ma 
from src.app.models.city import City


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(256), nullable=False)
    password = db.Column(db.String(256), nullable=False)
    
    id_city = db.Column(db.Integer, db.ForeignKey(City.id), nullable=False)

    def __init__(self, name, age, email, password, id_city) -> None:
        self.name = name
        self.age = age
        self.id_city = id_city
        self.email = email
        self.password = password
    


class UserSchema(ma.Schema):
    class Meta:
        Fields = ("id", "name", "age", "email", "password", "id_city")


user_share_schema = UserSchema()
users_share_schema = UserSchema(many=True)

