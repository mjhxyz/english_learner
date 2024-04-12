import datetime
from . import BaseModel

from app.ext import db


class Collection(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    obj_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String, nullable=False)
    cn = db.Column(db.String, nullable=False, default=str)
    type = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    add_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
