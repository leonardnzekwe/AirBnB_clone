#!/usr/bin/python3
"""
FileStorage Test Module:
a class that serializes instances to a JSON file
and deserializes JSON file to instances
"""


import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os.path import exists


class FileStorage:
    """
    FileStorage class:
    a class that serializes instances to a JSON file
    and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}
    classes_dict = {
        "BaseModel": BaseModel, "User": User, "State": State,
        "City": City, "Amenity": Amenity, "Place": Place,
        "Review": Review
    }

    def all(self):
        """
        all() method:
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        new() method:
        sets in __objects the obj with key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        save() method:
        serializes __objects to the JSON file (path: __file_path)
        """
        data = {}
        for key, obj in self.__objects.items():
            data[key] = obj.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(data, file)

    def reload(self):
        """
        reload() method:
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        otherwise, do nothing. If the file doesn't exist,
        no exception should be raised)
        """
        if exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                for key, obj_dict in data.items():
                    class_name = obj_dict["__class__"]
                    if class_name in FileStorage.classes_dict:
                        cls = FileStorage.classes_dict[class_name]
                        self.__objects[key] = cls(**obj_dict)
