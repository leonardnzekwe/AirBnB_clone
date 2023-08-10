#!/usr/bin/python3
"""
Review class Module:
a class that inherits from BaseModel
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class:
    Inherits from BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""
