from flask import Blueprint, render_template


from ext import cache

cache_blue = Blueprint('cache', __name__, template_folder='templates')

def init_cache_blue(app):
    app.register_blueprint(cache_blue, url_prefix='/cache1')

"""
三个参数
timeout  过期时间
key_prefix  缓存key的前缀
unless: 回调函数 当返回True 缓存不起作用  None 使用缓存

"""


@cache_blue.route('/1/')
@cache.cached(timeout=60, key_prefix='')
def test():
    print('hahaha')
    return '111'



#make_name  是一个函数  返回string类型  默认情况下函数名称作为key缓存起来

#有参数一定要用memoize
@cache_blue.route('/2/<name>/')
@cache.memoize(timeout=60 * 60)
def test1(name):
    print(name)
    return '222'


@cache_blue.route('/3/')
def test2():
    return render_template('cache.html', msg='111')


