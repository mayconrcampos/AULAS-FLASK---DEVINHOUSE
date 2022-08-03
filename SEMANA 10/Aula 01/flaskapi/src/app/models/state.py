from itertools import count
from src.app.db import db, ma 
from src.app.models.country import Country

class State(db.Model):
    __tablename__ = "states"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    initials = db.Column(db.String(2), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey(Country.id), nullable=False)

    def __init__(self, name, initials, country_id) -> None:
        self.name = name
        self.initials = initials
        self.country_id = country_id


class StateSchema(ma.Schema):
    class Meta:
        Fields = ("id", "name", "initials", "country_id")


state_share_schema = StateSchema()
states_share_schema = StateSchema(many=True)