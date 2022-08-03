from src.app.db import db, ma 
from src.app.models.state import State

class City(db.Model):
    __tablename__ = "cities"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(128), nullable=False)

    id_state = db.Column(db.Integer, db.ForeignKey(State.id), nullable=False)

    def __init__(self, name, id_state) -> None:
        self.name = name
        self.id_state = id_state


class CitySchema(ma.Schema):
    class Meta:
        Fields = ("id", "name", "id_state")


city_share_schema = CitySchema()
cities_share_schema = CitySchema(many=True)