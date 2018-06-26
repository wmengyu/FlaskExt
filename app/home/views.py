from email.mime import image

from flask import Blueprint, app, request, render_template, jsonify

from app.utils.views import get_new_file_name
from ext import images

upload_blue = Blueprint('upload', __name__, template_folder='templates')



def init_upload(app):
    app.register_blueprint(upload_blue, url_prefix='/upload')

"""
文上传必须是post请求  form-data
"""


@upload_blue.route('/img/', methods=['GET', 'POST'])
def upload_img():
    # 文件上传对象  字典
    if request.method == 'GET':
        return render_template('/upload.html')

    elif request.method == 'POST':
        image = request.files['img']
        file_name = images.save(image, name=get_new_file_name(image.filename))
        #生成可以访问的路径
        url = images.url(file_name)
        return jsonify({'msg': 'success', 'status': 200, 'url': url})



