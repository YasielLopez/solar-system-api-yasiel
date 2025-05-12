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