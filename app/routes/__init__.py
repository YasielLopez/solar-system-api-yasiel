from flask import Blueprint, jsonify
from app.models import planet_list

planets_bp = Blueprint("planets", __name__)

@planets_bp.route("/planets", methods=["GET"])
def get_all_planets():
    planets_response = [planet.to_dict() for planet in planet_list]
    return jsonify(planets_response)
