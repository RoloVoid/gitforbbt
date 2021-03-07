from flask import session
import database
from extends import error
from flask import request, Blueprint

boardedit_bp = Blueprint('boardedit', __name__, url_prefix='/board/modification')


@boardedit_bp.route('', methods=['PUT'])
def edit_one_board():
    data = request.get_json(force=True)
    tempid = data.get('id')
    text = data.get('text')
    last = data.get('last')

    if tempid is '':
        raise error.error412

    # if text is "":
    #    raise error.error410

    tempid = int(tempid)

    username = session['username']
    print(username)
    sessiondb = database.session

    temp = sessiondb.query(database.Boards).filter(database.Boards.id == tempid,
                                                   database.Boards.username == username).first()
    if temp is None:
        raise error.error409
    # 判断给定的留言板是否存在

    temp.ltime = last
    temp.text = text
    # 更新留言板内容

    try:
        sessiondb.commit()
        return {
            "message": "修改成功"
        }
    except Exception:
        raise error.error411
