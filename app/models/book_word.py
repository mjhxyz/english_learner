from datetime import datetime
from app.ext import db
from . import BaseModel


class BookWord(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, nullable=False)
    word_id = db.Column(db.Integer, nullable=False)
    add_time = db.Column(db.DateTime, nullable=False, default=datetime.now)
