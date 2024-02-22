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
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, 'w') as file:
            dictionary_for_json = {}
            for key, obj in self.__objects.items():
                dictionary_for_json[key] = obj.to_dict()
            json.dump(dictionary_for_json, file)

    def reload(self):
        from models.base_model import BaseModel
        try:
            with open(self.__file_path, 'r') as file:
                dictionary_from_json = json.load(file)
                for key, obj_dictionary in dictionary_from_json.items():
                    self.__objects[key] = BaseModel(**obj_dictionary)
        except FileNotFoundError:
            pass