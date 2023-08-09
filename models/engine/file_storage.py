#!/usr/bin/python3
"""
FileStorage Test Module:
a class that serializes instances to a JSON file
and deserializes JSON file to instances
"""


import json
from os.path import exists


class FileStorage:
    """
    FileStorage class:
    a class that serializes instances to a JSON file
    and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

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
            from models.base_model import BaseModel

            with open(self.__file_path, "r") as file:
                data = json.load(file)
            self.__objects = {}
            for key, obj_dict in data.items():
                self.__objects[key] = BaseModel(**obj_dict)
