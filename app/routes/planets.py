from flask import Blueprint, jsonify, abort, make_response
from ..db import db
# from app.models import planet_list


# creates a blueprint for planet routes

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

# Since flask has been updated, need to use .get instead of .route ... ["GET"]
# @planets_bp.route("", methods=["GET"])
# def get_all_planets():
#     planets_response = [planet.to_dict() for planet in planet_list]
    # Don't need to use jsonify, should be able to return planets_reponse
    # return jsonify(planets_response)

@planets_bp.get("/<planet_id>")
def get_one_planet(planet_id):
    valid_planet = validate_planet(planet_id)
    return valid_planet.to_dict()
    # Don't need this because we have it in validate planet
    # for planet in planet_list:
    #     if planet.id == planet_id:
    #         return {
    #             "description": planet.description,
    #             "diameter_km": planet.diameter_km,
    #             "id": planet.id,
    #             "name": planet.name
    #         }
    # Don't need this error message because it is checked in validation function
    # return {"message": f"planet {planet_id} not found"}, 404

# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except:
#         response = {"message": f"planet {planet_id} invalid"}
#         abort(make_response(response, 400))

#     for planet in planet_list:
#         if planet.id == planet_id:
#             return planet

#     response = {"message": f"planet {planet_id} not found"}
#     abort(make_response(response, 404))
