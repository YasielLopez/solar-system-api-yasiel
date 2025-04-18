from flask import Blueprint
from ..models.planet import planets

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

'''
## RESTful Endpoints: Read
Create the following endpoint(s), with similar functionality presented in the Hello Books API:

As a client, I want to send a request...

1. ...to get all existing `planets`, so that I can see a list of `planets`, with their `id`, `name`, `description`, and other data of the `planet`.'''

# Create decorator to get all planets
@planets_bp.get("")
def get_all_planets(): # Create an api, aka endpoint, to get all existing planets
    # Initiazlie a list that will store existing planers
    planets_response = []
    # Loop through planets to append to planets_response
    for planet in planets:
        planets_response.append(
            {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description
            }
        )
    # Return list
    return planets_response