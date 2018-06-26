from flask import Flask
from app.cache01.views import init_cache_blue
from app.home.views import init_upload
from app.user.views import init_users
from app.visitor.views import init_visitor
from ext import init_ext

app = Flask(__name__)
app.debug = True

def get_app():
    register_blue()
    init_ext(app)
    return app

def register_blue():
    init_users(app)
    init_cache_blue(app)
    init_visitor(app)
    init_upload(app)
