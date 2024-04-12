from datetime import datetime

from app.ext import db
from . import BaseModel


class Word(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(80), unique=True, nullable=False)
    cn = db.Column(db.String(1024), nullable=False)
    add_time = db.Column(db.DateTime, nullable=False, default=datetime.now)
    update_time = db.Column(db.DateTime)
