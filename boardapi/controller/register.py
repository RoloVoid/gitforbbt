import database
from extends import error
from flask import request, Blueprint
from werkzeug.security import generate_password_hash

register_bp = Blueprint('register', __name__, url_prefix='/register')


@register_bp.route('', methods=['POST'])
def register():
    data = request.get_json(force=True)
    username = data.get('username')
    password = data.get('password')
    # 还是从request的json格式信息里获取注册信息，按下不表

    session = database.session
    # 获取来自数据库的连接

    if username is "" or password is "":
        raise error.error400

    temp = session.query(database.Privacy).filter(database.Privacy.username == username).first()
    if temp is not None:
        raise error.error406
    # 查重，保证用户名唯一

    ed_userprivacy = database.Privacy(username=username, password=generate_password_hash(password))
    session.add(ed_userprivacy)
    # 试图在登录数据库里增加记录

    ed_user = database.Users(username=username, nickname=username)
    session.add(ed_user)
    # 试图在用户信息数据库里增加记录,根据接口文档，如果昵称没修改就是用户名

    session.commit()
    # 提交所有记录

    return {
        "message": "注册成功"
    }
