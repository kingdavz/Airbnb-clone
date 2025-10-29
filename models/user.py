#!/usr/bin/python
"""A model for the user profile"""

from models.base_model import BaseModel

class User(BaseModel):
    """
    User class that inherits from BaseModel.
    Attributes:
        email (str): The email address of the user.
        password: an attribute that store password
        first_name: an attribute that store first name
        last_name: an attribute that store last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
