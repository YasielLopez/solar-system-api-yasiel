from flask import Blueprint, abort, make_response, request
from ..models.Planet import Planet
from ..db import db

# from app.models import planet_list


# creates a blueprint for planet routes
planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.post("")
def create_planet():
    # Request 
    request_body = request.get_json()
    name = request_body["name"]
    description = request_body["description"]
    diameter_km = request_body["diameter_km"]

    new_planet = Planet(name=name, description=description, diameter_km=diameter_km)
    db.session.add(new_planet)
    db.session.commit()
    # Response
    response = {
        "id": new_planet.id,
        "name": new_planet.name,
        "description": new_planet.description,
        "diameter_km": new_planet.diameter_km
    }
    return response, 201

@planets_bp.get("")
def get_all_planets():
    query = db.select(Planet).order_by(Planet.id)
    planets = db.session.scalars(query)
    # We could also write the line above as:
    # planets = db.session.execute(query).scalars()
    planets_response = []
    for planet in planets:
        planets_response.append(
            {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "diameter_km": planet.diameter_km
            }
        )
    return planets_response, 200


@planets_bp.get("/<planet_id>")
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)
    return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "diameter_km": planet.diameter_km
    }

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        response = {"message": f"planet {planet_id} invalid"}
        abort(make_response(response , 400))
    query = db.select(Planet).where(Planet.id == planet_id)
    planet = db.session.scalar(query)

    if not planet:
        response = {"message": f"planet {planet_id} not found"}
        abort(make_response(response, 404))
    return planet