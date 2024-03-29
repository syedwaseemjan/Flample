"""
    flample.frontend
    ~~~~~~~~~~~~~~~~~~

    launchpad frontend application package
"""

from functools import wraps

from flask import render_template
from flask_login import LoginManager, login_required

from flample import factory
from flample.frontend import assets
from flample.models import Admin

login_manager = LoginManager()


def create_app(settings_override=None):
    """Returns the Flample dashboard application instance"""
    app = factory.create_app(__name__, __path__, settings_override)

    login_manager.init_app(app)
    login_manager.login_view = "dashboard.login"

    # Init assets
    assets.init_app(app)

    # Register custom error handlers
    if not app.debug:
        for e in [500, 404]:
            app.errorhandler(e)(handle_error)

    return app


def handle_error(e):
    return render_template("errors/%s.html" % e.code), e.code


def route(bp, *args, **kwargs):
    def decorator(f):
        @bp.route(*args, **kwargs)
        @login_required
        @wraps(f)
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)

        return f

    return decorator


@login_manager.user_loader
def load_user(userid):
    return Admin.query.get(userid)
