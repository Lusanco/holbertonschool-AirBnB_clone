#!/usr/bin/python3

from models.user import User
from models.base_model import BaseModel

# Create an instance of the User class
user_instance = User()

# Validate inheritance with BaseModel
if isinstance(user_instance, BaseModel):
    print("Instance creation + validate inheritance with BaseModel: PASSED")
else:
    print("Instance creation + validate inheritance with BaseModel: FAILED")
