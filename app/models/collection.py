from app.ext import db


class Collection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    obj_id = db.Column(db.Integer, nullable=False)
    type = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    add_time = db.Column(db.DateTime, nullable=False)
