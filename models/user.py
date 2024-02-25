#!/usr/bin/python3
"""
Module: user
Descri: class User that inherits from BaseModel
Author: Livanhernandez, Lusanco
"""

from models.base_model import BaseModel


class User(BaseModel):
    """User Class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
