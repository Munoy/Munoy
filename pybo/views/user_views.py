from flask import Blueprint

bp = Blueprint('user', __name__, url_prefix='/user')

@bp.route('/')
def user_info():
    return 'All User BP'

@bp.route('/list')
def hello_pybo():
    return 'Hello, 사용자'

