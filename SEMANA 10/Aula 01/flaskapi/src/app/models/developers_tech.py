from email.policy import default
from src.app.db import db, ma 
from src.app.models.devs import Developer
from src.app.models.tech import Tech


class Dev_tech(db.Model):
    __tablename__ = "devtechs"
    
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    id_tech = db.Column(db.Integer, db.ForeignKey(Tech.id), nullable=False)
    id_dev = db.Column(db.Integer, db.ForeignKey(Developer.id), nullable=False)
    is_main_tech = db.Column(db.Boolean, nullable=False, default=False)


    def __init__(self, id_tech, id_dev, is_main_tech) -> None:
        self.id_tech = id_tech
        self.id_dev = id_dev
        self.is_main_tech = is_main_tech


class Dev_techSchema(ma.Schema):
    class Meta:
        Fields = ("id", "id_tech", "id_dev", "is_main_tech")



dev_tech_share_schema = Dev_techSchema()
dev_techs_share_schema = Dev_techSchema(many=True)