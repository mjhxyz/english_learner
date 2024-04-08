import json

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.json.provider import DefaultJSONProvider

from .view.index import index_bp
from .view.words import words_bp
from .api.words import words_api
from .ext import config_extensions
from .models import BaseModel

db = SQLAlchemy()


def config_blueprint(app):
    BLUEPRINTS = [
        (index_bp, '/'),
        (words_bp, '/words'),

        (words_api, '/api/words'),
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
