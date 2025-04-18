from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)
    
    # Configure the Flask app
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    # Register blueprints
    from app.routes.planets import planets_bp
    app.register_blueprint(planets_bp)
    
    @app.route("/")
    def home():
        return {"message": "Welcome to the Solar System API!"}
    
    return app