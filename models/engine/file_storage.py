#!/usr/bin/python
"""A module that serialize instance to a JSON file and
deserialize JSON """
import json
import sys
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity
import os





class Filestorage:
    """
     FileStorage class that serializes instances to a JSON file 
     and deserialize th JSON instances
     Attr:
     __file__path: a private attribute that holds the name of the file
     __objects: a private attributr that holds object
     method:
     new: a method that sets aprivate attribute with key and value
     reload: a method deserialize yhe JSON file to __objects
    """

    __file_path = "airbnb.json"
    __objects = {}
    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects
    
    def new(self, obj):
        """sets in __objects the obj with key <class name>
        """
        key = obj.__class__.__name__
        key += str(obj.id)
        self.__objects[key] = obj

    def reload(self):
        """Deserialize the JSON file
        """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, encoding= "utf-8") as f:
                my_dict = json.load(f)
                for key, value in my_dict.items():
                    name = sys.modules[__name__]
                    my_class = getattr(name, value["__class__"])
                    self.__objects[key] = my_class(**value)

    def save(self):
        """serialize objects to the JSON file"""
        j_dict = {}
        for key in self.__objects:
            j_dict[key] =self.__objects[key].to_dict()
            with open(self.__file_path, "w") as f:
                json.dump(j_dict,f)
                    
