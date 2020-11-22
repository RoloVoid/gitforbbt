from flask import Flask, jsonify
import config
from Util import HttpError
from controller.users import users_bp
from controller.add import add_bp


app = Flask(__name__)

app.config['SECRET_KEY'] = config.secret_key

app.register_blueprint(users_bp)
app.register_blueprint(add_bp)


@app.errorhandler(HttpError)
def handle_http_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


# 实质是错误页面的重定向

if __name__ == '__main__':
    app.run()
