from datetime import datetime

from app.ext import db
from . import BaseModel


class Book(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True, nullable=False)
    hot = db.Column(db.Integer, nullable=False, default=0)
    add_time = db.Column(db.DateTime, nullable=False, default=datetime.now)
    update_time = db.Column(db.DateTime)
