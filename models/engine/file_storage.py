#!/usr/bin/python3

"""
Module: file_storage
Descri: class FileStorage that serializes
instances to a JSON file and deserializes
JSON file to instances
Author: Livanhernandez, Lusanco
"""


import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Saves new obj on dict"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Saves JSON dict"""
        with open(self.__file_path, 'w') as file:
            json_dict = {}
        for key, obj in self.__objects.items():
            json_dict[key] = obj.to_dict()
            json.dump(json_dict, file)

    def reload(self):
        """Reloads JSON dict"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.amenity import Amenity
        from models.place import Place
        from models.city import City
        from models.review import Review

        __class_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "Amenity": Amenity,
            "Place": Place,
            "City": City,
            "Review": Review
            }
        try:
            with open(self.__file_path, 'r') as file:
                json_dictionary = json.load(file)
                for key, obj_dict in json_dictionary.items():
                    class_name = obj_dict["__class__"]
                    class_call = __class_dict[class_name]
                    self.__objects[key] = class_call(** obj_dict)

        except FileNotFoundError:
            pass
