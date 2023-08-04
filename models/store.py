from db import db

class StoreModel(db.model):
    __tablename__="store"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    items = db.relationship("ItemModel",back_populates="item", lazy="dynamic")
