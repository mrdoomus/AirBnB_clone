#!/usr/bin/python3
''' Module that defines BaseModel class
BaseModel - Sets every attribute and method for other classes
'''
import uuid
from datetime import datetime
import models


class BaseModel():
    ''' Sets every attribute and method for other classes '''

    def __init__(self, *args, **kwargs):
        ''' Initializes BaseModel objects
            @args: Arguments in tuples
            @kwargs:Arguments in dictionaries '''
        self.id = str(uuid.uuid4())
        self.updated_at = datetime.today()
        self.created_at = datetime.today()

        if kwargs is not {} and kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(
                        kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(
                        kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        ''' Converts into string a BaseModel object '''
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        ''' updates the public instance attribute
            updated_at with the current datetime '''
        self.updated_at = datetime.today()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        ''' returns a dictionary containing all
            keys/values of __dict__ of the instance '''
        base_dict = self.__dict__.copy()
        base_dict['__class__'] = self.__class__.__name__
        base_dict['updated_at'] = base_dict['updated_at'].isoformat()
        base_dict['created_at'] = base_dict['created_at'].isoformat()
        return base_dict
