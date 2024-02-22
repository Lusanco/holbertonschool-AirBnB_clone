#!/usr/bin/python3

"""
Module: review
Descri: class Review that inherits from BaseModel
Author: Livanhernandez, Lusanco
"""


from models.base_model import BaseModel


class Review(BaseModel):
    place_id = "" # Place.id
    user_id = "" # User.id
    text = ""
