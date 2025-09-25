from flask import Blueprint, jsonify, request
from app.services.ai_service import gen_analysis, gen_hints
from app.services.auth import check_access_key
analyze_bp = Blueprint('analyze', __name__)

@analyze_bp.route('/analyze',methods=["POST"])
@check_access_key
def analyze_code():
    data = request.get_json()
    genresponse = gen_analysis(data)
    return jsonify(genresponse)  

@analyze_bp.route("/gotstuck", methods=["POST"])
@check_access_key
def gotstuck():
    data = request.get_json()
    genhints = gen_hints(data)
    return jsonify(genhints)