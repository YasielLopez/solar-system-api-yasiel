from flask import Blueprint, jsonify
from app.models import planet_list


# creates a blueprint for planet routes

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])
def get_all_planets():
    planets_response = [planet.to_dict() for planet in planet_list]
    return jsonify(planets_response)

@planets_bp.route("<id>", methods=["GET"])
def get_one_planet(id):
    pass

def validate_planet(id):
    tri: id = inct()
except value

def make_responses(invalid, 400)
return planet 


