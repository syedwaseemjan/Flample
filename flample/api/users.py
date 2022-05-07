from flask import Blueprint, jsonify, redirect
from flask_login import login_user

from flample.decorators import logout_required
from flample.forms import LoginForm

bp = Blueprint("users", __name__)


@bp.route("/login", methods=["POST"])
@logout_required
def login():
    form = LoginForm()
    if form.validate_on_submit():
        login_user(form.user, remember=form.remember.data)
        return redirect("/")
    return jsonify({"success": False})
