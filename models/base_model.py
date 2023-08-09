#!/usr/bin/python3
"""
BaseModel class Module:
A class that defines all common attributes/methods for other classes
"""


from datetime import datetime
from models import storage
from uuid import uuid4


class BaseModel:
    """
    BaseModel class:
    that defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        __init__() method:
        Initialize instance attributes based on keyword arguments or defaults.
        If no kwargs are provided, default values will be used.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """
        __str__() method:
        string represention of the BaseModel object
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        save() method:
        updates the public instance attribute updated_at
        with the current datetime
        also calls save(self) method of storage
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        to_dict() method:
        returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        instance_dict = self.__dict__.copy()
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()
        return instance_dict
