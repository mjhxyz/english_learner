from flask_login import current_user
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask import redirect

db = SQLAlchemy()


# 初始化拓展
def config_extensions(app):
    # 数据库
    db.init_app(app)
    # 登录
    login_manager = LoginManager(app)

    @login_manager.user_loader
    def load_user(user_id):
        from .models.user import User
        return User.query.get(int(user_id))

    @app.context_processor
    def inject_user():
        return {'user': current_user}

    @login_manager.unauthorized_handler
    def unauthorized():
        return redirect('/users/login')
