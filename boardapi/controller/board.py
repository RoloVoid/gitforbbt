import database
from flask import Blueprint
import json

board_bp = Blueprint('board', __name__, url_prefix='/boards/all')


@board_bp.route('', methods=['GET'])
def get_all_boards():
    sessiondb = database.session

    temp = sessiondb.query(database.Boards).all()
    data = {}
    counter = 0
    for instance in temp:
        board = {'nickname': instance.nickname, 'id': instance.id, 'message': instance.text}
        data[str(counter)] = board
        counter += 1

    response = json.dumps({"boards": data})

    print(response)

    return response
# 简单地把所有的留言板都扒出来然后展示
