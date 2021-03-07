from flask import session
import database
from extends import error
from flask import request, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash

userinfoedit_bp = Blueprint('userinfoedit', __name__, url_prefix='/userinfo/modification')


@userinfoedit_bp.route('', methods=['POST'])
def update_user_info():
    data = request.get_json(force=True)
    username = session['username']
    age = data.get('age')
    nickname = data.get('nickname')
    gender = data.get('gender')
    # 老套的从请求体里扒数据

    sessiondb = database.session
    # 调用数据库连接

    temp1 = sessiondb.query(database.Users).filter(database.Users.nickname == nickname).first()

    if temp1 is not None:
        raise error.error407
    # 先确定昵称没被人使用

    user_info = sessiondb.query(database.Users).filter(database.Users.username == username).first()
    # 获得条目

    if nickname is not '':
        user_info.nickname = nickname
    if age is not '':
        user_info.age = int(age)
    if gender is not '':
        user_info.gender = gender
    # 修改条目

    password = data.get('password')
    if password is not "":
        privacy_info = sessiondb.query(database.Privacy).filter(database.Privacy.username == username).first()
        privacy_info.password = generate_password_hash(password)
        # 若要密码有修改，则提交

    sessiondb.commit()
    # 提交修改

    return {
        "username": session['username'],
        "message": "个人信息修改成功"
    }
