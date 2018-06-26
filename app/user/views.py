

from flask import Blueprint, render_template, request, redirect, url_for, abort

from flask_login import login_manager, login_user, login_required, logout_user

from app.user.models import User
from ext import db, login_manager
from app.user.models import User
from werkzeug.security import generate_password_hash, check_password_hash


user = Blueprint('user', __name__, static_folder='static', template_folder='templates')


def init_users(app):
    app.register_blueprint(user, url_prefix='/user')


"""
1. 登录   注销功能
2. 限制用户的权限
3. 记住密码功能
4. 对session进行保护
"""


@login_manager.user_loader
def init_user(uid):
    user = User.query.get(uid)
    return user

@user.route('/login/', methods=['POST', 'GET'])
def login():
    msg = None
    if request.method == 'GET':
        return render_template('/login.html')
    elif request.method == 'POST':
        uid = request.values.get('uid')
        username = request.values.get('username')
        password = request.values.get('pwd')
        if username and password and uid:
            try:
                user = db.session.query(User.uid, User.username, User.password,  User.email,  User.is_active).first()
                if user:
                    if user.password == password:
                        # 必须调用第三方插件login_user表示用户登录成功
                        login_user(user)
                        return redirect(url_for('/index/'))
                    else:
                        msg = '密码错误'
                else:
                    msg = '用户不存在'
            except Exception as e:
                print(e)
                msg = '网络异常,请检查网络'
        else:
           msg = '不支持的请求方式'
        return render_template('/login.html', msg)

@user.route('/loginout/', methods=['POST', 'GET'])
def login_out():
    login_user()
    return redirect(url_for('login'))


@user.route('/test/')
@login_required
def test():
    return render_template('index.html')