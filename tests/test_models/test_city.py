#!/usr/bin/python3
''' Test for class City '''
import unittest
from unittest import mock
from io import StringIO
import json
import pep8
import inspect
import datetime
import os
from models.engine.file_storage import FileStorage
from models import city
City = city.City


class TestCityDoc(unittest.TestCase):
    '''
    calss to check documentation for City class
    '''

    @classmethod
    def setUpClass(cls):
        ''' This method run before all test and
            find into City class all functions.
            it store in a list of tuples
        '''
        cls.list_base_functions = inspect.getmembers(
            City, inspect.isfunction)

    def test_pep8_city_class(self):
        ''' Test that models/city.py conforms to PEP8 '''
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found pep8 erros and warnings in city.py")

    def test_pep8_city_test(self):
        ''' Test that test/test_models/test_city.py conforms to PEP8 '''
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ['tests/test_models/test_city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found pep8 erros and warnings in test_city.py")

    def test_module_documentation(self):
        ''' check module documentation '''
        doc = True
        try:
            len(city.__doc__) >= 1
        except Exception:
            doc = False
        mesg = "No documentation found for {} module"
        self.assertEqual(
            True, doc, mesg.format(city.__name__))

    def test_class_documentation(self):
        ''' check class City documentation '''
        doc = True
        try:
            len(City.__doc__) >= 1
        except Exception:
            doc = False
        mesg = "No documentation found for {} class"
        self.assertEqual(
            True, doc, mesg.format(city.__name__))

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


class TestCity(unittest.TestCase):
    ''' Test for City class '''
    @classmethod
    def setUpClass(cls):
        cls.path_file = 'file.json'
        cls.list_objects = [City, City,
                            City, City, City]

    def setUp(self):
        FileStorage._FileStorage__objects = {}
        if os.path.exists(self.path_file):
            os.remove(self.path_file)

    def tearDown(self):
        FileStorage._FileStorage__objects = {}
        if os.path.exists(self.path_file):
            os.remove(self.path_file)

    def test_id_str(self):
        base = City()

        self.assertIsInstance(base.id, str)

        self.assertIsInstance(base.id, str)

    def test___file_path_exists(self):
        self.assertEqual(FileStorage._FileStorage__file_path, self.path_file)

    def test__objects_exists(self):
        self.assertEqual(FileStorage._FileStorage__objects, {})

    def test_datetime(self):
        base = City()
        self.assertIsInstance(base.created_at, datetime.datetime)
        self.assertIsInstance(base.updated_at, datetime.datetime)

    def test_create_object_simple(self):
        base = City()
        base.name = "Holberton"
        base.my_number = 89
        self.assertTrue(base.id)
        self.assertTrue(base.name)
        self.assertTrue(base.my_number)

    def test_create_object_args(self):
        base = City('name', 'Holberton')
        list_expected = list(base.__dict__.values())
        list_fail = list_expected + ['name', 'Holberton']
        self.assertNotEqual(list_expected, list_fail)

    def test_create_object_kwargs(self):
        base = City(name='name', school='Holberton')
        self.assertTrue(base.name)
        self.assertTrue(base.school)
        self.assertEqual(base.name, 'name')
        self.assertEqual(base.school, 'Holberton')

    def test_create_object_simple_storage(self):
        base = City()
        storage = FileStorage()
        dict_obects = storage.all()
        self.assertEqual(base, dict_obects['City.' + base.id])

    def test_create_object_kwargs_storage(self):
        data = {'name': 'name', 'school': 'Holberton'}
        base = City(**data)
        storage = FileStorage()
        self.assertDictEqual(storage.all(), {})

    def test__str__(self):
        base = City()
        base.name = 'test'
        base.email = 'test@mail.com'
        str_rep = str(base)
        expected = "[{}] ({}) {}".format(
            base.__class__.__name__, base.id, base.__dict__)
        self.assertEqual(str_rep, expected)

    def test_str_output(self):
        base = City()
        base.name = 'test'
        base.email = 'test@mail.com'
        expected = "[{}] ({}) {}".format(
            base.__class__.__name__, base.id, base.__dict__)
        with mock.patch('sys.stdout', new=StringIO()) as std_out:
            print(str(base))
            output = std_out.getvalue()
            self.assertEqual(output.strip(), expected.strip())

    def test_to_dict(self):
        storage = FileStorage()
        base = City()
        base.name = 'test'
        base.email = 'test@mail.com'
        to_dict = base.to_dict()
        expected = base.__dict__.copy()
        expected['__class__'] = base.__class__.__name__
        expected['updated_at'] = expected['updated_at'].isoformat()
        expected['created_at'] = expected['created_at'].isoformat()
        self.assertDictEqual(to_dict, expected)

    def test_to_dict_output(self):
        dt = datetime.datetime.today()
        base = City()
        base.id = "123456"
        base.created_at = base.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'City',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(base.to_dict(), tdict)

    def test_save_exists_file(self):
        base = City()
        base.save()
        self.assertTrue(os.path.exists(self.path_file))

    def test_save_test_content(self):
        base = City()
        base.name = 'test'
        base.email = 'test@mail.com'
        base.save()
        self.assertTrue(os.path.exists(self.path_file))
        dict_to_load = {}
        with open(self.path_file, 'r') as reader:
                dict_to_load = json.loads(reader.read())
        self.assertDictEqual(
            base.to_dict(), dict_to_load['City.' + base.id])
