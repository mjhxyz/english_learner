from flask import current_app, jsonify
from flask_login import current_user


def admin_required(f):
    def wrap(*args, **kwargs):
        if not current_user.is_authenticated:
            return current_app.login_manager.unauthorized()
        if current_user.rid != 1:
            return jsonify(code=36, message='permission denied')
        return f(*args, **kwargs)

    return wrap
