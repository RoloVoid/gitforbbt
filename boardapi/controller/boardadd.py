from flask import session
import database
from extends import error
from flask import request, Blueprint
import datetime

add_bp = Blueprint('add', __name__, url_prefix='/board/add')


@add_bp.route('', methods=['POST'])
def add_one_board():
    username = session['username']
    # 调用当前登录的用户名，以此作为索引在数据库添加数据

    data = request.get_json(force=True)
    text = data.get('text')
    date = data.get('date')
    last = data.get('last')
    # 获取前端传过来的文本

    sessiondb = database.session
    # 调用数据库连接

    now = datetime.datetime.now()
    ed_board = database.Boards(username=username, text=text, ptime=date, ltime=last)
    # 构造留言板对象，检查之后写到数据库里去

    sessiondb.add(ed_board)
    # 提交修改

    if text is None or text is "":
        raise error.error410
    # 为了保证不会被空留言板挤占空间

    try:
        sessiondb.commit()
        return {"message": "添加成功"}
    except Exception:
        raise error.error411
    # 处理文本过长而无法写入的问题
