import json

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .view.index import index_bp
from .view.words import words_bp
from .view.books import books_bp
from .view.user import users_bp
from .view.admin.user import admin_user_bp
from .view.admin.words import admin_words_bp
from .view.admin.books import admin_books_bp
from .view.collection import collection_bp
from .api.words import words_api
from .api.books import books_api
from .api.admin.words import admin_words_api
from .api.collection import collection_api
from .ext import config_extensions
from .models import BaseModel

db = SQLAlchemy()


def config_blueprint(app):
    BLUEPRINTS = [
        (index_bp, '/'),
        (words_bp, '/words'),
        (books_bp, '/books'),
        (users_bp, '/users'),
        (admin_user_bp, '/admin/user'),
        (collection_bp, '/collection'),
        (admin_words_bp, '/admin/words'),
        (admin_books_bp, '/admin/books'),

        (words_api, '/api/words'),
        (books_api, '/api/books'),
        (collection_api, '/api/collection'),
        (admin_words_api, '/api/admin/words'),
    ]
    for bp, prefix in BLUEPRINTS:
        app.register_blueprint(bp, url_prefix=prefix)


def create_app():
    app = Flask(__name__)
    # TODO 按照环境 加载配置
    app.config.from_object('app.config.DevelopmentConfig')
    # 加载依赖扩展
    config_extensions(app)
    # 加载蓝图
    config_blueprint(app)

    return app
