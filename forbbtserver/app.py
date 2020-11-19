from flask import Flask, request, jsonify, session
from mysql.connector import connect
import database
app = Flask(__name__)

secret_key = '123456'

app.config['SECRET_KEY'] = secret_key


class HttpError(Exception):
    def __init__(self, status_code, message):
        super().__init__()
        self.message = message
        self.status_code = status_code

    def to_dict(self):
        return {
            'message': self.message,
            'status_code': self.status_code
        }


@app.route('/add', methods=['POST'])
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


@app.route('/users', methods=['GET'])
def get_user_list():
    con, cursor = connect_to_database()
    cursor.execute('select `username` from users')
    userslist = cursor.fetchall()

    temp = {}
    for i in userslist:
        temp[i[0]] = None
    # return值不能为list，所以改为dictionary
    session['userslist'] = temp

    cursor.close()
    con.close()

    return session['userslist']


@app.errorhandler(HttpError)
def handle_http_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


# 实质是错误页面的重定向

if __name__ == '__main__':
    app.run()
