#!/usr/bin/python3

"""
Module: file_storage
Descri: class FileStorage that serializes
instances to a JSON file and deserializes
JSON file to instances
Author: Livanhernandez, Lusanco
"""


import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """Return objects"""
        return self.__objects

    def new(self, obj):
        """Saves new obj on dict"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Saves JSON dict"""
        from models import storage
        with open(self.__file_path, "w") as file:
            dictionary_for_json = {}
            for key, obj in self.__objects.items():
                dictionary_for_json[key] = obj.to_dict()
            json.dump(dictionary_for_json, file)

    def reload(self):
        """Reloads JSON dict"""
        from models.base_model import BaseModel
        try:
            with open(self.__file_path, 'r') as file:
                loaded_objs = json.load(file)
                for key, obj_dictionary in loaded_objs.items():
                    class_name, obj_id = key.split('.')
                    if class_name == "User":
                        obj_instance = User(**obj_dictionary)
                    elif class_name == "BaseModel":
                        obj_instance = BaseModel(**obj_dictionary)
                    else:
                        continue
                    self.__objects[key] = obj_instance
        except FileNotFoundError:
            pass
