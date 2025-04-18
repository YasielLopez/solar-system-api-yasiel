from flask import Blueprint
from ..models.planet import planets

planet_bp = Blueprint("", __name__, url_prefix="/planets")

'''
## RESTful Endpoints: Read
Create the following endpoint(s), with similar functionality presented in the Hello Books API:

As a client, I want to send a request...

1. ...to get all existing `planets`, so that I can see a list of `planets`, with their `id`, `name`, `description`, and other data of the `planet`.'''

# Create decorator to get all planets
@planet_bp.get("")
def get_all_planets():
    return planets