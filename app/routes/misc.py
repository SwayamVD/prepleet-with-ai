from flask import Blueprint

misc_bp = Blueprint('misc', __name__)

@misc_bp.route('/')
def home():
    return {'message': 'home endpoint'}
