from flask import Blueprint, jsonify, request
from app.services.ai_service import gen_analysis, gen_hints

analyze_bp = Blueprint('analyze', __name__)

@analyze_bp.route('/analyze',methods=["POST"])
def analyze_code():
    data = request.get_json()
    genresponse = gen_analysis(data)
    return jsonify(genresponse)  

@analyze_bp.route("/gotstuck", methods=["POST"])
def gotstuck():
    data = request.get_json()
    genhints = gen_hints(data)
    return jsonify(genhints)