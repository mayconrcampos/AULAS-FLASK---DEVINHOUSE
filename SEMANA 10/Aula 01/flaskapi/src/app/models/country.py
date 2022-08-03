from src.app.db import db, ma

class Country(db.Model):
    __tablename__ = "countrys"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    language = db.Column(db.String(64), nullable=False)

    def __init__(self, name, language) -> None:
        self.name = name
        self.language = language


class CountrySchema(ma.Schema):
    class Meta:
        Fields = ("id", "name", "language")


country_share_schema = CountrySchema()
countrys_share_schema = CountrySchema(many=True)