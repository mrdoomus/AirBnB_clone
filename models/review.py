#!/usr/bin/python3
''' Module that manage Review
'''

# aplication imports
from models.base_model import BaseModel


class Review(BaseModel):
    ''' Review that inherits from BaseModel '''

    place_id = ""
    user_id = ""
    text = ""
