#!/usr/bin/python3

"""
Module: city
Descri: class City that inherits from BaseModel
Author: Livanhernandez, Lusanco
"""


from models.base_model import BaseModel


class City(BaseModel):
    state_id = "" # State.id
    name = ""
