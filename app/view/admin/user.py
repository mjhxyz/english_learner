from flask import Blueprint, render_template, request, jsonify
from sqlalchemy import and_, or_

from . import admin_required
from app.models.user import User, db

admin_user_bp = Blueprint('/admin/user', __name__)


@admin_user_bp.route('/', methods=['GET'])
@admin_required
def index():
    return render_template('admin/user.j2')


@admin_user_bp.route('/list', methods=['GET'])
@admin_required
def _list():
    args = request.args
    page = int(args['page'])
    limit = int(args['limit'])
    keyword = args.get('keyword')
    q = User.query
    if keyword:
        q = q.filter(or_(User.login_id.like('%' + keyword + '%'), User.name.like('%' + keyword + '%')))
    page_result = q.paginate(page=page, per_page=limit)
    items = list(map(lambda x: x.to_dict(), page_result.items))
    data = {
        "code": 0,
        "msg": "",
        "count": page_result.total,
        "data": items
    }
    return jsonify(data)


@admin_user_bp.route('/add', methods=['GET'])
def add():
    return render_template('admin/form/user/add.j2')


@admin_user_bp.route('/do_add', methods=['POST'])
def do_add():
    data = request.json
    user = User.query.filter_by(login_id=data['login_id']).first()
    if user:
        return jsonify({'ok': True, 'msg': '登录名已存在'})
    user = User()
    user.login_id = data['login_id']
    user.name = data['name']
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'ok': True})


@admin_user_bp.route('/delete', methods=['POST'])
def delete():
    data = request.json
    record_id = data['id']
    User.query.filter(and_(User.id == record_id, User.rid != 1)).delete()
    db.session.commit()
    return jsonify({'ok': True})
