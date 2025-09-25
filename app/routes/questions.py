from flask import Blueprint, jsonify
from app.services.auth import check_access_key
from app.services.question_loader import load_questions, get_companies_name
questions_bp = Blueprint('questions', __name__)

@questions_bp.route('/questions/<company>')
@check_access_key
def get_questions(company):
    all_questions = load_questions(company=company)
    return jsonify(all_questions)


@questions_bp.route('/getcompanylist')
@check_access_key
def get_cmp_list():
    cmplist = get_companies_name()
    return jsonify(cmplist)

