'''
    This creates a class of a Planet object. There are 3 attributes:
    name, deacription, and diameter in kilometers. There is a method 
    that creates a dictionary with Planet attributes. 
    Programmer: Yasiel Lopez
'''

from sqlalchemy.orm import Mapped, mapped_column
from ..db import db

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    diameter_km: Mapped[int]
# class Planet:
#     def __init__(self, id, name, description, diameter_km):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.diameter_km = diameter_km
    
#     # creates a to_dict() method that converts the object to a dictionary format suitable for JSON responses
#     def to_dict(self):
#         return {
#             "id": self.id,
#             "name": self.name,
#             "description": self.description,
#             "diameter_km": self.diameter_km
#         }
