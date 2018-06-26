import os

from flask_caching import Cache
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#实例化sqlalchemy对象
from flask_uploads import UploadSet, IMAGES, configure_uploads, patch_request_class

db = SQLAlchemy()
#实例化迁移对象
migrate = Migrate()

#所有的第三方插件的配置总方法
def init_ext(app):
    #配置数据库
    config_db(app)
    #初始化SQLALCHEMY
    db.init_app(app)
    #注册迁移命令
    migrate.init_app(app=app, db=db)
    #初始化用户管理模块
    init_login_config(app)
    init_cache_config(app)
    #初始化文件上传
    init_upload_config(app)

#配置连接数据库的参数
def config_db(app):
    #配置数据库连接的url地址

    # 地址格式  数据库类型名+驱动://用户名:密码@ip地址:端口/数据库名?key=value
    # 例如 mysql + pymysql://root:root@127.0.0.1:3306/flask?charset=utf8
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SECRET_KEY'] = '13131231321'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/flask-ext?charset=utf8'



cache=Cache()

#缓存配置
def init_cache_config(app):
    cache.init_app(app, config={
        'CACHE_DEFAULT_TIMEOUT': 60,
        'CACHE_TYPE': 'redis',
        'CACHE_REDIS_HOST': '127.0.0.1',
        'CACHE_REDIS_PORT': '6379',
        # 'CACHE_REDIS_PASSWORD':'123456'
        'CACHE_REDIS_DB': 1,
        'CACHE_KEY_PREFIX': 'view_',
    })

#用户模块插件
login_manager = LoginManager()


#用户模块
def init_login_config(app):
    #当用户点击某个需要登录才能访问的界面的时候,
    #如果没有登录,就会自动跳转到相应视图函数
    login_manager.login_view = 'login'
    login_manager.login_message = '必须要登录才能访问'
    login_manager.init_app(app)

#文件上传相关配置
"""
参数说明
name: 保存文件子目录   默认是files
extensions: 设置允许上传的文件的类型   默认类型
default_dest: 设置文件上传的根路径 


"""


images = UploadSet(name='images', extensions=IMAGES, default_dest=None)

# xxx/static/upload/files
# 动态获取项目的根目录

# 配置信息
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_ROOT_PATH = os.path.join(BASE_DIR, 'static/upload')




#配置上传文件的根目录
def init_upload_config(app):
    # 配置上传的根目录
    app.config['UPLOADS_DEFAULT_DEST'] = UPLOAD_ROOT_PATH
    #生成文件的访问url地址
    app.config['UPLOADS_DEFAULT_URL'] = 'http://127.0.0.1:9000/static/upload'
    configure_uploads(app=app, upload_sets=images)
    #限制文件上传的大小
    patch_request_class(app=app, size=16 * 1024 * 1024)