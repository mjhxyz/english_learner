from flask import Blueprint, render_template, request, flash, redirect
from flask_login import login_user, logout_user

from ..models.user import User, db

users_bp = Blueprint('users', __name__)


@users_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = request.form
    method = request.method
    if method == 'GET':
        return render_template('register.j2')
    # 判断两次密码是否一样
    login_id = form.get('login_id')
    name = form.get('name')
    pwd = form.get('pwd')
    rePwd = form.get('rePwd')
    if pwd != rePwd:
        # 消息闪现
        flash('密码不匹配!', 'error')
        return render_template('register.j2')
    # 检查 login id 是否存在
    user = User.query.filter_by(login_id=form.get('login_id')).first()
    if user is not None:
        flash('用户已经存在!', 'error')
        return render_template('register.j2')
    # 插入到数据库
    user = User(login_id=login_id, name=name, rid=2)
    user.set_password(pwd)
    db.session.add(user)
    db.session.commit()
    return redirect('/users/login')


@users_bp.route('/login', methods=['GET', 'POST'])
def login():
    method = request.method
    if method == 'GET':
        return render_template('login.j2')
    # 登录
    form = request.form
    login_id = form.get('login_id')
    user = User.query.filter_by(login_id=login_id).first()
    if user is None:
        flash('用户不存在', 'error')
        return render_template('login.j2')
    if user.validate_password(form.get('pwd')):
        login_user(user)
        return redirect('/')
    flash('账号或密码错误', 'error')
    return render_template('login.j2')


@users_bp.route('/exit', methods=['GET', 'POST'])
def exit():
    logout_user()
    return redirect('/')
