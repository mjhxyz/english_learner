from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

import datetime

from app.ext import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login_id = db.Column(db.String(32), unique=True, nullable=False)
    name = db.Column(db.String(32), unique=True, nullable=False)
    pwd = db.Column(db.String(200), nullable=False)
    rid = db.Column(db.Integer, nullable=False)
    add_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    update_time = db.Column(db.DateTime)

    def set_password(self, password):
        self.pwd = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.pwd, password)
