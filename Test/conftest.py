import pytest
from app import create_app
from app.db import db
from flask.signals import request_finished
from app.models.Planet import Planet
from dotenv import load_dotenv
import os

load_dotenv()

@pytest.fixture
def app():
    test_config = {
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": os.environ.get('SQLALCHEMY_TEST_DATABASE_URI')
    }
    app = create_app(config=test_config)

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def two_saved_planets(app):
    # Arrange
    mercury = Planet(
        name="Mercury", 
        description="The smallest planet in our solar system",
        diameter_km=4879
    )
    venus = Planet(
        name="Venus", 
        description="The hottest planet in our solar system",
        diameter_km=12104
    )

    with app.app_context():
        db.session.add_all([mercury, venus])
        db.session.commit()
    
        # We need to get the IDs after commit
        planets = [mercury, venus]
        yield planets