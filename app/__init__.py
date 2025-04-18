from flask import Flask
# Import planet blueprint
from .routes.planet_routes import planets_bp

# def create_app(test_config=None):
def create_app():
    app = Flask(__name__)

    # register planet blueprint
    app.register_blueprint(planets_bp)

    return app
