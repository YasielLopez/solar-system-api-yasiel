from flask import Blueprint, abort, make_response, request
from ..models.Planet import Planet
from ..models.Moon import Moon
from ..db import db


# creates a blueprint for planet routes
planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.post("")
def create_planet():
    # Request 
    request_body = request.get_json()
    try:
        new_planet = Planet.from_dict(request_body)
    except KeyError as error:
        response = {"message": f"Invalid request: missing {error.args[0]}"}
        abort(make_response(response, 400))
    db.session.add(new_planet)
    db.session.commit()
    
    return new_planet.to_dict(), 201

@planets_bp.get("")
def get_all_planets():
    query = db.select(Planet)

    description_param = request.args.get("description")
    if description_param:
        query = query.where(Planet.description.ilike(f"%{description_param}%"))

    # diameter filtering
    min_diameter = request.args.get("min_diameter")
    max_diameter = request.args.get("max_diameter")
    
    if min_diameter:
        try:
            min_diameter = float(min_diameter)
            query = query.where(Planet.diameter_km >= min_diameter)
        except ValueError:
            pass
    
    if max_diameter:
        try:
            max_diameter = float(max_diameter)
            query = query.where(Planet.diameter_km <= max_diameter)
        except ValueError:
            pass
    
    query = query.order_by(Planet.id)
    planets = db.session.scalars(query)
    planets_response = []
    for planet in planets:
        planets_response.append(planet.to_dict())

    return planets_response, 200


@planets_bp.get("/<planet_id>")
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)
    return planet.to_dict(), 200

@planets_bp.delete("/<planet_id>")
def delete_planet(planet_id):
    planet = validate_planet(planet_id)
    
    db.session.delete(planet)
    db.session.commit()
    
    return {"message": f"Planet {planet_id} successfully deleted"}, 200

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

# NESTED ROUTES
# @planets_bp.post("/<planet_id>/moons")
# def add_new_moon(planet_id):
#     planet = validate_planet(planet_id)
#     request_body = request.get_json()
#     request_body["planet_id"] = planet.id
#     return create_model(Moon, request_body)

# @planets_bp.get("/<planet_id>/moons")
# def get_books_by_author(planet_id):
#     planet = validate_planet(Planet, planet_id)
#     response = [moon.to_dict() for moon in planet.moons]
#     return response


def create_model(cls, model_data):
    try:
        new_model = cls.from_dict(model_data)
        
    except KeyError as error:
        response = {"message": f"Invalid request: missing {error.args[0]}"}
        abort(make_response(response, 400))
    
    db.session.add(new_model)
    db.session.commit()

    return new_model.to_dict(), 201
