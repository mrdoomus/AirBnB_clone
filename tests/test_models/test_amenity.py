#!/usr/bin/python3
''' Test for class Amenity '''
import unittest
from unittest import mock
from io import StringIO
import json
import pep8
import inspect
import datetime
import os
from models import amenity
from models.engine.file_storage import FileStorage
Amenity = amenity.Amenity


class TestAmenityDoc(unittest.TestCase):
    '''
    calss to check documentation for Amenity class
    '''

    @classmethod
    def setUpClass(cls):
        ''' This method run before all test and
            find into Amenity class all functions.
            it store in a list of tuples
        '''
        cls.list_base_functions = inspect.getmembers(
            Amenity, inspect.isfunction)

    def test_pep8_amenity_class(self):
        ''' Test that models/amenity.py conforms to PEP8 '''
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found pep8 erros and warnings in amenity.py")

    def test_pep8_amenity_test(self):
        ''' Test that test/test_models/test_amenity.py conforms to PEP8 '''
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ['tests/test_models/test_amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found pep8 erros and warnings in test_amenity.py")

    def test_module_documentation(self):
        ''' check module documentation '''
        doc = True
        try:
            len(amenity.__doc__) >= 1
        except Exception:
            doc = False
        mesg = "No documentation found for {} module"
        self.assertEqual(
            True, doc, mesg.format(amenity.__name__))

    def test_class_documentation(self):
        ''' check class Amenity documentation '''
        doc = True
        try:
            len(Amenity.__doc__) >= 1
        except Exception:
            doc = False
        mesg = "No documentation found for {} class"
        self.assertEqual(
            True, doc, mesg.format(Amenity.__name__))

    def test_functions(self):
        ''' check documentation for every function '''
        for item in self.list_base_functions:
            function = item[1]
            doc = True
            try:
                len(function.__doc__) >= 1
            except Exception:
                doc = False
            mesg = "No documentation found for < def {} > function"
            self.assertEqual(
                True, doc, mesg.format(function.__name__))


class TestAmenity(unittest.TestCase):
    ''' Test for Amenity class '''
    @classmethod
    def setUpClass(cls):
        cls.path_file = 'file.json'

    def setUp(self):
        FileStorage._FileStorage__objects = {}
        if os.path.exists(self.path_file):
            os.remove(self.path_file)

    def tearDown(self):
        FileStorage._FileStorage__objects = {}
        if os.path.exists(self.path_file):
            os.remove(self.path_file)

    def test___file_path_exists(self):
        self.assertEqual(FileStorage._FileStorage__file_path, self.path_file)

    def test__objects_exists(self):
        self.assertEqual(FileStorage._FileStorage__objects, {})

    def test_all(self):
        storage = FileStorage()
        self.assertEqual(storage.all(), {})

    def test_new(self):
        base = Amenity()
        storage = FileStorage()
        storage.new(base)
        self.assertNotEqual(storage.all(), {})

    def test_save_exists_file(self):
        base = Amenity()
        base.save()
        self.assertTrue(os.path.exists(self.path_file))

    def test_save_test_content(self):
        base = Amenity()
        base.name = 'test_storage'
        base.email = 'save@mail.com'
        base.save()
        self.assertTrue(os.path.exists(self.path_file))
        dict_to_load = {}
        with open(self.path_file, 'r') as reader:
                dict_to_load = json.loads(reader.read())
        self.assertDictEqual(
            base.to_dict(), dict_to_load['Amenity.' + base.id])

    def test_reload(self):
        storage = FileStorage()
        base = Amenity()
        base.name = 'test_storage'
        base.email = 'save@mail.com'
        base.save()
        FileStorage._FileStorage__objects = {}
        storage.reload()
        self.assertNotEqual(storage.all(), {})
