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
        serialized_objs = {}
        for key, obj in self.__objects.items():
            serialized_objs[key] = obj.to_dict() if hasattr(obj, "to_dict") else obj

        with open(self.__file_path, "w") as file:
            json.dump(serialized_objs, file)

    def reload(self):
        try:
            with open(self.__file_path, "r") as file:
                file_content = file.read()
                if file_content:
                    self.__objects = json.loads(file_content)
        except (FileNotFoundError, json.JSONDecodeError):
            pass
