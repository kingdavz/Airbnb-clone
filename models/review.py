#!/usr/bin/python
"""A module that handles review class"""

from models.base_model import BaseModel

class Review(BaseModel):
    """
    Review class that inherits from BaseModel
    Attr:
        place_id: an attribute that stores place id
        user_id: an attribute that stores user id
        text: an attribute that stores review of clients
    """
    place_id = ""
    user_id = ""
    text = ""
