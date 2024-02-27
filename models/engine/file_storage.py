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
        json_dict = {}
        for key, obj in FileStorage.__objects.items():
            json_dict[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(json_dict, file)

    def reload(self):
        """Reloads JSON dict"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        try:
            with open(self.__file_path, 'r') as file:
                json_dictionary = json.load(file)
                for key, value in json_dictionary.items():
                    class_name = value["__class__"]
                    if class_name == 'User':
                        obj = class_name(**value)
                        self.__objects[key] = obj
                    elif class_name == "BaseModel":
                        obj = class_name(**value)
                        self.__objects[key] = obj
                    elif class_name == "Place":
                        obj = class_name(**value)
                        self.__objects[key] = obj
                    elif class_name == "State":
                        obj = class_name(**value)
                        self.objects[key] = obj
                    elif class_name == "City":
                        obj = class_name(**value)
                        self.objects[key] = obj
                    elif class_name == "Amenity":
                        obj = class_name(**value)
                        self.objects[key] = obj
                    elif class_name == "Review":
                        obj = class_name(**value)
                        self.objects[key] = obj
                    
        
        except FileNotFoundError:
            pass
