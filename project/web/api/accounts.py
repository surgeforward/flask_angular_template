from flask import Blueprint
from flask_jwt import jwt_required, current_user

from ...resources.services import accounts
from . import route

bp = Blueprint('accounts', __name__, url_prefix='/accounts')

@route(bp, '/')
@jwt_required
def whoami():
    return current_user

@route(bp, '/<id>')
def show(id):
    return accounts.get_or_404(id)