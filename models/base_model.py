#!/usr/bin/python3

"""
Module: base_model
Descri: class BaseModel that defines all
common attributes/methods for other classes
Author: Livanhernandez, Lusanco
"""


from datetime import datetime
import uuid


class BaseModel:
    """BaseModel Class"""

    def __init__(self, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        return "[{}] ({}) {}".format("BaseModel", self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        result = self.__dict__.copy()
        result["__class__"] = self.__class__.__name__
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        return result
