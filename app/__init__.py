from flask import Flask

from .view.index import index_bp
from .view.words import words_bp
from .api.words import words_api


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
    # 加载配置
    # app.config.from_object('config.Config')
    # 加载蓝图
    config_blueprint(app)
    return app
