import database
from Util import HttpError
from flask import Blueprint, request

add_bp = Blueprint('add', __name__, url_prefix='/add')


@add_bp.route('', methods=['POST'])
def add_to_database():
    userdata = request.get_json(force=True)

    username = userdata.get('name')
    SID = userdata.get('num')

    con, cursor = database.connect_to_database()

    if username is None and SID is None:
        raise HttpError(400, "缺少参数 name\n 缺少参数 num")
    elif username is None:
        raise HttpError(400, "缺少参数 name")
    elif SID is None:
        raise HttpError(400, "缺少参数 num")
    # http错误问题处理

    cursor.execute('select count(*) from `users` where `userID`=%s', (SID,))
    count = cursor.fetchone()
    # 用游标返回一个记录，若记录首项ID>1显然存在记录
    if count[0] >= 1:
        raise HttpError(400, "该用户已存在")

    cursor.execute('insert into `users`(`username`, `userID`) values (%s, %s)',
                   (username, SID))
    con.commit()

    cursor.close()
    con.close()

    return "添加成功"
