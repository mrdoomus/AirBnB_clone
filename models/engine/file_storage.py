#!/usr/bin/python3
""" serialization-deserialization module """
# python imports
import json
import os.path
# aplication imports
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """ Class for store data to file"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj
            with key <obj class name>.id """
        to_dict = obj.to_dict()
        key = to_dict['__class__'] + '.' + to_dict['id']
        new_dict = {key: obj}
        self.__objects.update(**new_dict)

    def save(self):
        """ serializes __objects to the
            JSON file (path: __file_path) """
        dict_to_save = {key: value.to_dict()
                        for (key, value) in self.__objects.items()}
        with open(self.__file_path, 'w') as f_writer:
            f_writer.write(json.dumps(dict_to_save))

    def reload(self):
        """ deserializes the JSON file to __objects """
        dict_to_load = {}
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as reader:
                dict_to_load = json.loads(reader.read())

        for key, value in dict_to_load.items():
            instance_object = globals()[value['__class__']](**value)
            self.new(instance_object)
