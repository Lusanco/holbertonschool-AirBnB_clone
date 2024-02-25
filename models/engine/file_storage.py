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
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Saves JSON dict"""
        with open(self.__file_path, "w") as file:
            dictionary_for_json = {}
            for key, obj in self.__objects.items():
                dictionary_for_json[key] = obj.to_dict()
            json.dump(dictionary_for_json, file)

    def destroy(self, obj):
        """
        Delete obj from __objects and update the JSON file
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]
                self.save()  # Save the updated dictionary to the JSON file

    def reload(self):
        """Reloads JSON dict"""
        from models.base_model import BaseModel

        try:
            with open(self.__file_path, "r") as file:
                dictionary_from_json = json.load(file)
                for key, obj_dictionary in dictionary_from_json.items():
                    self.__objects[key] = BaseModel(**obj_dictionary)
        except FileNotFoundError:
            pass
