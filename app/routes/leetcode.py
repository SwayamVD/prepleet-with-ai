from flask import Blueprint, jsonify
from app.services.leetcode_api import get_favorite_set,get_problem_details,get_problem_set
leetcode_bp = Blueprint('leetcode', __name__)

@leetcode_bp.route('/prepleet/problem/<slug>')
def fetchdetails(slug):
    details = get_problem_details(slug=slug)
    return jsonify(details)

@leetcode_bp.route('/prepleet/set/<search>')
def fetchset(search):
    details = get_problem_set(search=search)
    return jsonify(details)

@leetcode_bp.route('/prepleet/fav/<name>')
def fetchfav(name):
    details = get_favorite_set(fname=name)
    return jsonify(details)