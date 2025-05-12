'''
    This creates a Moon model. There is a one to many relationship with the Planet model. Use relationship to create a bidirectional connection between the two models. Create ForeignKey relationship with planet_id.
    Programmer: Laura
'''
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import Optional
from ..db import db

class Moon(db.Model):
    id: Mapped[int]=mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    diameter_km: Mapped[int]
    planet_id: Mapped[int]= mapped_column(ForeignKey("planet.id"))
    planet: Mapped[Optional["Planet"]] = relationship(back_populates="moons")

    def to_dict(self):
        moon_as_dict = {}
        moon_as_dict["id"] = self.id
        moon_as_dict["name"] = self.name
        moon_as_dict["description"] = self.description
        moon_as_dict["diameter_km"] = self.diameter_km
        return moon_as_dict
    
    @classmethod
    def from_dict(cls, moon_data):
        moon = Moon(name=moon_data["name"], 
                    description=moon_data["description"],
                    diameter_km=moon_data["diameter_km"],
                    planet_id=moon_data["planet_id"])
        return moon