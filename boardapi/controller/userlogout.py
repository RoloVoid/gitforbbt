from flask import session
from flask import request, Blueprint

logout_bp = Blueprint('logout', __name__, url_prefix="/userinfo/logout")


@logout_bp.route('', methods=['POST'])
def log_out_current_user():
    data = request.get_json(force=True)
    username = data.get('username')


    session['username'] = None

    return {
        "message": "注销成功"
    }
