from flask import Flask, jsonify, render_template
from util import HttpError
import config
from controller.register import register_bp
from controller.session import session_bp
from controller.boardadd import add_bp
from controller.userinfoedit import userinfoedit_bp
from controller.board import board_bp
from controller.boardmodification import boardedit_bp
from controller.boarddeletion import boarddelete_bp
from controller.info import info_bp
from controller.userlogout import logout_bp

app = Flask(__name__)

app.config['SECRET_KEY'] = config.secret_key

app.register_blueprint(register_bp)
app.register_blueprint(session_bp)
app.register_blueprint(add_bp)
app.register_blueprint(userinfoedit_bp)
app.register_blueprint(boardedit_bp)
app.register_blueprint(boarddelete_bp)
app.register_blueprint(board_bp)
app.register_blueprint(info_bp)
app.register_blueprint(logout_bp)


@app.route('/')
def start_page():
    return render_template('enter.html')


@app.route('/session')
def log_in_template():
    return render_template('login.html')


@app.route('/allboards')
def guest_page():
    return render_template('guest_board.html')


@app.route('/board')
def user_page():
    return render_template('board.html')


@app.route('/register')
def register_page():
    return render_template('register.html')


@app.route('/user')
def user_info_page():
    return render_template('person.html')


@app.errorhandler(HttpError)
def handle_http_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


if __name__ == '__main__':
    app.run()
