from flask import Flask
# Import planet blueprint
from .routes.planet_routes import planet_bp


def create_app(test_config=None):
    app = Flask(__name__)

    # register planet blueprint
    app.register_blueprint(planet_bp)
    return app
