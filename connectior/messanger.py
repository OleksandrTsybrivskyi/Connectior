from flask import Blueprint, render_template

bp = Blueprint('messanger', __name__)


@bp.route('/messanger')
def messanger():
    return render_template("messanger.html")