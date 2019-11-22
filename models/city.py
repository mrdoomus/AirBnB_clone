#!/usr/bin/python3
''' Module that manage City
'''

# aplication imports
from models.base_model import BaseModel


class City(BaseModel):
    ''' City that inherits from BaseModel '''
    state_id = ""
    name = ""
