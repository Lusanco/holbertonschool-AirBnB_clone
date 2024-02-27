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
        return self.__objects

    def new(self, obj):
        """Saves new obj on dict"""
        name_class = obj.__class__.__name__
        key_obj = str(name_class = "." + obj.id)
        self.__objects[key_obj] = obj

    def save(self):
        """Saves JSON dict"""
        json_dict = {}
        for key, value in FileStorage.__objects.items():
            json_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as file:
            json.dump(json_dict, file)

    def reload(self):
        """Reloads JSON dict"""
        from models.base_model import BaseModel
        try:
            with open(FileStorage.__file_path, mode='r', encoding="utf-8") as file:
                json_dictionary = json.load(file)
                for key, value in json_dictionary.items():
                    class_name, obj_id = key.split(".")
                    obj_dict = value
                    obj_dict["__class__"] = class_name
                    obj = eval(class_name)(**obj_dict)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
