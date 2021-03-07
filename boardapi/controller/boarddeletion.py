import database
from extends import error
from flask import request, Blueprint, session

boarddelete_bp = Blueprint('boarddelete', __name__, url_prefix='/board/deletion')


@boarddelete_bp.route('', methods=['POST'])
def delete_one_board():
    data = request.get_json(force=True)
    tempid = data.get("id")

    sessiondb = database.session

    if tempid is '':
        raise error.error412

    tempid = int(tempid)

    username = session['username']
    # 获取当前登录的用户

    temp = sessiondb.query(database.Boards).filter(database.Boards.username == username,
                                                   database.Boards.id == tempid).first()

    if temp is None:
        raise error.error409
    # 判断当前用户名下是否存在该留言板

    sessiondb.query(database.Boards).filter(database.Boards.username == username,
                                            database.Boards.id == tempid).delete()
    # 删除留言板

    sessiondb.commit()

    return {
        "message": "删除成功"
    }
