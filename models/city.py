#!/usr/bin/python3
"""
City class Module:
a class thar inherits from BaseModel
"""


from models.base_model import BaseModel


class City(BaseModel):
    """
    City class:
    Inherits from BaseModel
    """
    state_id = ""
    name = ""
