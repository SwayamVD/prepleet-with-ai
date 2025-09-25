from flask import Flask


def create_app():
    app = Flask(__name__)
    from app.routes.questions import questions_bp
    from app.routes.analyze import analyze_bp
    from app.routes.leetcode import leetcode_bp
    from app.routes.misc import misc_bp

    app.register_blueprint(questions_bp)
    app.register_blueprint(analyze_bp)
    app.register_blueprint(leetcode_bp)
    app.register_blueprint(misc_bp)

    return app
