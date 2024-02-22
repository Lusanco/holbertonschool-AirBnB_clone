#!/usr/bin/python3

"""
Module: base_model
Descri: class BaseModel that defines all
common attributes/methods for other classes
Author: Livanhernandez, Lusanco
"""


from models import storage
from datetime import datetime
import uuid


class BaseModel:
    """BaseModel Class"""

    def __init__(self, *args, **kwargs):
        """Instance method that initializes a new object"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "__class__":
                    continue  # Skip setting __class__ as an attribute
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """Returns str in representation of an object"""
        return "[{}] ({}) {}".format("BaseModel", self.id, self.__dict__)

    def save(self):
        """Saves datetime and JSON file storage in storage"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Copies dictionary"""
        result = self.__dict__.copy()
        result["__class__"] = self.__class__.__name__
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        return result
