from flask import Blueprint, session
import database

users_bp = Blueprint('users', __name__, url_prefix='/users')


@users_bp.route('', methods=['GET'])
def get_user_list():
    con, cursor = database.connect_to_database()
    cursor.execute('select `username` from users')
    userslist = cursor.fetchall()

    temp = "[\n"
    for i in userslist:
        temp = temp + "\""+i[0]+"\"" + "\n"
    temp = temp+"]"

    # return值不能为list，所以改为String输出
    session['userslist'] = temp

    cursor.close()
    con.close()

    return session['userslist']
