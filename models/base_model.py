#!/usr/bin/python
"""A base model class for all models in our application."""

from datetime import datetime
from uuid import uuid4
import models

class BaseModel:
    """
    BaseModel class serve as a base for
    other model class.
    Method:
       save: a method that update an instance attribute
       to_dict: a method that returns a dictionary repr.
       __str__: a magic method that prints class as a string
    """
    def __init__(self, *args, **kwargs):
        """
        class constructor with public instances
            *args: Unused.
            **kwargs: Key/value pairs of attributes.
        """
        
        if len(kwargs) > 0:
            for attr, value in kwargs.items():
                if attr == "created_at" or attr == "updated_at":
                    setattr(self, attr, datetime.fromisoformat(value))
                elif attr == "__class__":
                    pass
                else:
                    setattr(self, attr, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self) 
            

    def __str__(self):
        """Print the representation of the object."""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                        self.id, self.__dict__)
    
    def save(self):
        """Update the instance attribute."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """A MODULE THAT CONVERT TO DICTIONARY"""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict["created_at"] = self.created_at.isoformat()
        return my_dict