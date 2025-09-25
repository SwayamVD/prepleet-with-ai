from flask import Blueprint, jsonify
from app.services.leetcode_api import get_favorite_set,get_problem_details,get_problem_set
from app.services.auth import check_access_key
leetcode_bp = Blueprint('leetcode', __name__)

@leetcode_bp.route('/prepleet/problem/<slug>')
@check_access_key
def fetchdetails(slug):
    details = get_problem_details(slug=slug)
    return jsonify(details)

@leetcode_bp.route('/prepleet/set/<search>')
@check_access_key
def fetchset(search):
    details = get_problem_set(search=search)
    return jsonify(details)

@leetcode_bp.route('/prepleet/fav/<name>')
@check_access_key
def fetchfav(name):
    details = get_favorite_set(fname=name)
    return jsonify(details)