#!/usr/bin/python3
''' Module that manage State
'''

# aplication imports
from models.base_model import BaseModel


class State(BaseModel):
    ''' State that inherits from BaseModel '''
    name = ""
