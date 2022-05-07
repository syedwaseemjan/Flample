"""
    flample.api
    ~~~~~~~~~~~~~

    flample api application package
"""

from functools import wraps

from flask import jsonify
from flask_login import LoginManager, login_required

from flample import factory
from flample.exceptions import FlampleError, FlampleFormError
from flample.models import Admin
from flample.utils import JSONEncoder

login_manager = LoginManager()


def create_app(settings_override=None, register_security_blueprint=False):
    """Returns the Flample API application instance"""

    app = factory.create_app(
        __name__,
        __path__,
        settings_override,
        register_security_blueprint=register_security_blueprint,
    )
    login_manager.init_app(app)
    # Set the default JSON encoder
    app.json_encoder = JSONEncoder

    # Register custom error handlers
    app.errorhandler(FlampleError)(on_flample_error)
    app.errorhandler(FlampleFormError)(on_flample_form_error)
    app.errorhandler(404)(on_404)

    return app


def route(bp, *args, **kwargs):
    kwargs.setdefault("strict_slashes", False)

    def decorator(f):
        @bp.route(*args, **kwargs)
        @login_required
        @wraps(f)
        def wrapper(*args, **kwargs):
            sc = 200
            rv = f(*args, **kwargs)
            if isinstance(rv, tuple):
                sc = rv[1]
                rv = rv[0]
            return jsonify(dict(data=rv)), sc

        return f

    return decorator


def on_flample_error(e):
    return jsonify(dict(error=e.msg)), 400


def on_flample_form_error(e):
    return jsonify(dict(errors=e.errors)), 400


def on_404(e):
    return jsonify(dict(error="Not found")), 404


@login_manager.unauthorized_handler
def unauthorized():
    return jsonify({"error": "Unauthorized access"}), 401


@login_manager.user_loader
def load_user(userid):
    return Admin.query.get(userid)
