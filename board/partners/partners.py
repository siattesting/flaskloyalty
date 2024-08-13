from flask import Blueprint, render_template

bp = Blueprint('partners', __name__, template_folder='templates')

@bp.route("/partners")
def partners():
    return render_template("partners/partners.html")

