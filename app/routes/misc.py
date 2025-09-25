from flask import Blueprint,render_template

misc_bp = Blueprint('misc', __name__)

@misc_bp.route('/')
def home():
    message = {
        "Get List of Companies": "/getcompanylist",
        "Get Companies Specific Questions": "/questions/<companyname>",
        "Problem Detail": "/prepleet/problem/<slug>",
        "Search Problem": "/prepleet/set/<search>",
        "Favourite Set": "/prepleet/fav/<name>",
    }
    return render_template("api-guide.html")
