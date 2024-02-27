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
                if key != "__class__":
                    if key == "created_at" or key == "update_at":
                        setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Returns str in representation of an object"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Saves the current instance to the storage"""
        from models import storage
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Copies dictionary"""
        result = self.__dict__.copy()
        result["__class__"] = self.__class__.__name__
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        return result

    def reload(self):
        from models import storage
        all_objects = storage.all()
        key = "{}.{}".format(self.__class__.__name__, self.id)
        if key in all_objects:
            obj = all_objects[key]
            self.__dict__.update(obj.__dict__)
