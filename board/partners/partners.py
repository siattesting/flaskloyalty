from flask import Blueprint, render_template, request

bp = Blueprint('partners', __name__, template_folder='templates')

@bp.route("/partners")
def partners():
    search = request.args.get('q')
    if search is not None:
        partners_set = []
    else:
        partners_set = []
    return render_template("partners/partners.html", partners=partners_set)

