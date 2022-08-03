from dataclasses import fields
from email.policy import default
from src.app.db import db, ma
from src.app.models.user import User

class Developer(db.Model):
    __tablename__ = "developers"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    months_experience = db.Column(db.Integer, nullable=False)
    accepted_remote_work = db.Column(db.Boolean, nullable=False, default=True)
    id_user = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)

    def __init__(self, months_experience, accepted_remote_work, id_user) -> None:
        self.months_experience = months_experience
        self.accepted_remote_work = accepted_remote_work
        self.id_user = id_user


class DeveloperSchema(ma.Schema):
    class Meta:
        fields = ("id", "months_experience", "accepted_remote_work", "id_user")


developer_share_schema = DeveloperSchema()
developers_share_schema = DeveloperSchema(many=True)