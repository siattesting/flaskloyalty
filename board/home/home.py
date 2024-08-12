from flask import Blueprint, render_template

bp = Blueprint('home', __name__, template_folder='templates')

@bp.route("/")
def home():
    return render_template("home/home.html")

@bp.route("/about")
def about():
    return render_template("home/about.html")