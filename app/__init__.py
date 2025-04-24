from flask import Flask
from .db import db, migrate

def create_app(test_config=None):
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/solar_system_development'

    db.init_app(app)
    migrate.init_app(app, db)
    
    # Register blueprints
    from app.routes.planets import planets_bp
    app.register_blueprint(planets_bp)
    
    @app.route("/")
    def home():
        return {"message": "Welcome to the Solar System API!"}
    
    return app