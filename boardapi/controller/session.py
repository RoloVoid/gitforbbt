import database
from extends import error
from flask import request, Blueprint, session
from werkzeug.security import check_password_hash

# 这个接口同时初始化了用户登录表和用户信息表

session_bp = Blueprint('session', __name__, url_prefix='/session')


@session_bp.route('', methods=['POST'])
def login():
    data = request.get_json(force=True)
    username = data.get('username')
    password = data.get('password')
    # 读取请求信息

    if username is "" or password is "":
        raise error.error400

    sessiondb = database.session
    # 获取来自数据库的连接

    temp = sessiondb.query(database.Privacy).filter(database.Privacy.username == username).first()
    if temp is None:
        raise error.error408
    elif check_password_hash(temp.password, password) is False:
        raise error.error408

    session['username'] = username

    return {"message": "登陆成功"}
    # 数据库里若无相关记录，或者密码错误，返回408错误
