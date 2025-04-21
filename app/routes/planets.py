from flask import Blueprint, jsonify, abort, make_response
from app.models import planet_list


# creates a blueprint for planet routes

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])
def get_all_planets():
    planets_response = [planet.to_dict() for planet in planet_list]
    return jsonify(planets_response)

<<<<<<< HEAD
@planets_bp.route("<id>", methods=["GET"])
def get_one_planet(id):
    pass

def validate_planet(id):
    tri: id = inct()
except value

def make_responses(invalid, 400)
return planet 


=======
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
>>>>>>> 8f78c8a4f4926b52687953ac70a0cbb78fa65ad5
