import pytest
from app.db import db
from app.models.Planet import Planet

# @pytest.mark.skip
def test_from_dict_returns_book():
    # Arrange
    planet_data = {
        "name": "New Moon",
        "description": "A satelite recently found in space",
        "diameter_km": 5879
    }

    # Act
    new_planet = Planet.from_dict(planet_data)

    # Assert
    assert new_planet.name == "New Moon"
    assert new_planet.description == "A satelite recently found in space"
    assert new_planet.diameter_km == 5879

def test_to_dict_returns_planet():
    # Arrange
    planet_data = Planet(id = 1,
                        name="Pluto",
                        description="Used to be a planet",
                        diameter_km=1240)

    # Act
    result = planet_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] == "Pluto"
    assert result["description"] == "Used to be a planet"
    assert result["diameter_km"] == 1240

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
def test_get_planets(client):

    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == [] 
# POST /planets with a JSON request body returns a 201

def test_get_planets_returns_list_with_seeded_planet(client, one_planet):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()
    
    # Assert
    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body[0]["id"] == one_planet.id
    assert response_body[0]["name"] == one_planet.name
    assert response_body[0]["description"] == one_planet.description
    assert response_body[0]["diameter_km"] == one_planet.diameter_km

def test_create_planet_with_valid_data(client):
    # Arrange
    new_planet_data = {
        "name": "Earth",
        "description": "The only known planet with life",
        "diameter_km": 12742
    }
    
    # Act
    response = client.post("/planets", json=new_planet_data)
    response_body = response.get_json()
    
    # Assert
    assert response.status_code == 201
    assert "id" in response_body
    assert response_body["name"] == new_planet_data["name"]
    assert response_body["description"] == new_planet_data["description"]
    assert response_body["diameter_km"] == new_planet_data["diameter_km"]
