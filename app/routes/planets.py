from flask import Blueprint, jsonify
from app.models import planet_list

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])
def get_all_planets():
    """
    Get a list of all planets
    """
    planets_response = [planet.to_dict() for planet in planet_list]
    return jsonify(planets_response)