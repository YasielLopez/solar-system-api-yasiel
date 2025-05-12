'''
    This creates a class of a Planet object. There are 3 attributes:
    name, deacription, and diameter in kilometers. There is a method 
    that creates a dictionary with Planet attributes. 
    Programmer: Yasiel Lopez
'''

from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    diameter_km: Mapped[int]
    moons: Mapped[list["Moon"]] = relationship(back_populates="planet")

    @classmethod
    def from_dict(cls, planet_data):
        planet = Planet(name=planet_data["name"], 
                        description=planet_data["description"],
                        diameter_km=planet_data["diameter_km"],
                        moons=planet_data["moons"])
        return planet

    def to_dict(self):
        planet_as_dict = {}
        planet_as_dict["id"] = self.id
        planet_as_dict["name"] = self.name
        planet_as_dict["description"] = self.description
        planet_as_dict["diameter_km"] = self.diameter_km
        planet_as_dict["moons"] = self.moons
        return planet_as_dict