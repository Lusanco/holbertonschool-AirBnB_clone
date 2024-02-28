#!/usr/bin/python3

"""
Module: file_storage
Descri: class FileStorage that serializes instances to a JSON
file and deserializes JSON file
to instances
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

    def reload(self):  # Reloads objects from the JSON file.
        from models.base_model import BaseModel
        from models.user import User
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State

        try:
            with open(FileStorage.__file_path, "r") as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name = value["__class__"]
                    if class_name == "BaseModel":
                        cls = BaseModel
                    elif class_name == "User":
                        cls = User
                    elif class_name == "Amenity":
                        cls = Amenity
                    elif class_name == "City":
                        cls = City
                    elif class_name == "Place":
                        cls = Place
                    elif class_name == "Review":
                        cls = Review
                    elif class_name == "State":
                        cls = State
                    else:
                        continue
                    obj = cls(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            return
