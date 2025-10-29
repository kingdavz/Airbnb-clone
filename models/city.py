#!/usr/bin/python
"""A module that handles city data"""

from models.base_model import BaseModel

class City(BaseModel):
    """
    City class that inherits from BaseModel
    Attr:
        state_id: a public attribute that stores state id
        name: a public attribute that stores name of city
    """
    state_id = ""
    name = ""