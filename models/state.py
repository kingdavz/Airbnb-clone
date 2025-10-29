#!/usr/bin/python
"""A module that handles state class"""

from models.base_model import BaseModel

class State(BaseModel):
    """
    State class that inherits the BaseModel
    Attr:
        name a public attribute that stores name of state
     """
    name = ""