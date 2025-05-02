from app.db import db
from app.models.Planet import Planet

def test_get_all_planets_returns_with_no_records(client):
    # act
    response = client.get("/planets")

    # assert
    assert response.status_code == 200
    assert response.get_json() == []

# GET /planets/1 returns a response body that matches our fixture
def test_get_one_planet_returns_seeded_planet(client, one_planet):
    # act
    response = client.get(f"/planets/{one_planet.id}")
    response_body = response.get_json()

    # assert
    assert response.status_code == 200
    assert response_body["id"] == one_planet.id
    assert response_body["name"] == one_planet.name
    assert response_body["description"] == one_planet.description
    assert response_body["diameter_km"] == one_planet.diameter_km
# GET /planets/1 with no data in test database (no fixture) returns a 404
def test_no_data_returns_404(client, one_planet):
    # act
    response = client.get("/planets/100")
    response_body = response.get_json()

    # assert
    assert response.status_code == 404
# GET /planets with valid test data (fixtures) returns a 200 with an array including appropriate test data
# POST /planets with a JSON request body returns a 201