"""
    runserver
    ~~~~

    flample wsgi module
"""

from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

from flample import api, frontend

application = DispatcherMiddleware(frontend.create_app(), {"/api": api.create_app()})

if __name__ == "__main__":
    run_simple("0.0.0.0", 5000, application, use_reloader=True, use_debugger=True)
