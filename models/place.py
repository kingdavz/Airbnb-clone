#!/usr/bin/python
"""A module that handles place properties """

from models.base_model import BaseModel

class Place(BaseModel):
    """
    Place class that inherits from BaseModel
    Attr:
        city_id: an attribute that stores city id
        user_id: an attribute that stores user id
        name: an attribute that stores name of place
        description: an attribute that stores description of place
        number_rooms: an attribute that stores number of rooms
        number_bathrooms: an attribute that stores number of bathrooms
        max_guest: an attribute that stores maximum number of guests
        price_by_night: an attribute that stores price by night
        latitude: an attribute that stores latitude of place
        longitude: an attribute that stores longitude of place
        amenity_ids: a list that store all amenity ids
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
