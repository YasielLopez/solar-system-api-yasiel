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

