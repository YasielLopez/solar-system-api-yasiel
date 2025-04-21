from flask import Blueprint, jsonify, abort, make_response
from app.models import planet_list


# creates a blueprint for planet routes

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])
def get_all_planets():
    """
    Get a list of all planets
    """
    planets_response = [planet.to_dict() for planet in planet_list]
    return jsonify(planets_response)

@planets_bp.get("/<planet_id>")
def get_one_planet(planet_id):
    planet_id = validate_planet(planet_id)

    for planet in planet_list:
        if planet.id == planet_id:
            return {
                "description": planet.description,
                "diameter_km": planet.diameter_km,
                "id": planet.id,
                "name": planet.name
            }
    return {"message": f"planet {planet_id} not found"}, 404

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        response = {"message": f"planet {planet_id} invalid"}
        abort(make_response(response, 400))

    for planet in planet_list:
        if planet.id == planet_id:
            return planet

    response = {"message": f"planet {planet_id} not found"}
    abort(make_response(response, 404))