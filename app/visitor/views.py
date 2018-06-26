from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, login_required, logout_user

from app.user.models import User
from ext import login_manager, db

from werkzeug.security import generate_password_hash, check_password_hash


visitor = Blueprint('visitor', __name__, static_folder='static', template_folder='templates')


def init_visitor(app):
    app.register_blueprint(visitor, url_prefix='/vis')



@login_manager.user_loader
def init_user(uid):
    user = User.query.get(uid)
    generate_password_hash('password')
    check_password_hash('password')
    return user

@visitor.route('/home/')
def home_page():
    return render_template('/home.html')

#登录
@visitor.route('/login1/', methods=['POST', 'GET'])
def login1():
    if request.method == 'GET':
        return render_template('/login1.html')
    elif request.method == 'POST':
        users = User.query.all()
        name = request.values.get('name')
        password = request.values.get('password')
        password1 = request.values.get('password1')

        if name in users.username:
            return render_template('/home.html')
        else:
            new_user = User(username=name, password=password)
            db.session.add(new_user)
            db.session.commit()
            msg = '注册成功'
            return render_template('/home.html', msg=msg, password1=password1)


    else:
        msg = '不支持的请求方式'

    return render_template('/login1.html/')



@visitor.route('/register/', methods=['POST', 'GET'])
def register1():
    if request.method == 'GET':
        return render_template('/register1.html/')
    elif request.method == 'POST':
        name = request.values.get('name')
        password = request.values.get('password')
        if name:
            user = User.query.filter(User.username == name).first()
            if user:
                return render_template('/home.html')
            else:
                msg = '注册成功'

        else:
            msg = '内容不能为空'
    else:
        msg = '不支持的请求方式'

    return render_template('/home.html', msg=msg)

@visitor.route('/loginout/', methods=['POST', 'GET'])
def logout():
    logout_user()
    return redirect(url_for('visitor.home_page'))


@visitor.route('/test/')
@login_required
def test():
    return render_template('/home.html')