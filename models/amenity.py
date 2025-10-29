#!/usr/bin/python
""""A module that handles amenity """

from models.base_model import BaseModel

class Amenity(BaseModel):
    """
    Amenity class that inherits from BaseModel
    Attr:
        name:  stores the name of amenity in house
    """
    name = ""