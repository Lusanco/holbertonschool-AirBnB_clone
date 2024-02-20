#!/usr/bin/python3

"""
Module: file_storage
Descri: class FileStorage that serializes
instances to a JSON file and deserializes
JSON file to instances
Author: Livanhernandez, Lusanco
"""


import json
from os.path import isfile


class FileStorage:
    __file__path = __name__ + ".json"
    __objects = {}

    def all(self):
        return self.__objects
    
    def new(self, obj):
        return
    
    def save(self):
        return
    
    def reload(self):
        return