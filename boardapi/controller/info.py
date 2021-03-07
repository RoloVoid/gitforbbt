from flask import session
import database
from flask import Blueprint

info_bp = Blueprint('info', __name__, url_prefix='/userinfo')


@info_bp.route('', methods=['GET'])
def get_user_info():
    username = session['username']

    sessiondb = database.session

    temp = sessiondb.query(database.Users).filter(database.Users.username == username).first()

    return {
        "username": temp.username,
        "age": temp.age,
        "gender": temp.gender,
        "nickname": temp.nickname
    }
