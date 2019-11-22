#!/usr/bin/python3
''' Test for class FileStorage '''
import unittest
import os
import json
import pep8
import inspect
from models.engine import file_storage
from models.base_model import BaseModel
FileStorage = file_storage.FileStorage


class TestFileStorageDoc(unittest.TestCase):
    '''
    calss to check documentation for FileStorage class
    '''

    @classmethod
    def setUpClass(cls):
        ''' This method run before all test and
            find into FileStorage class all functions.
            it store in a list of tuples
        '''
        cls.list_base_functions = inspect.getmembers(
            FileStorage, inspect.isfunction)

    def test_pep8_file_storage_class(self):
        ''' Test that models/file_storage.py conforms to PEP8 '''
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found pep8 erros and warnings in file_storage.py")

    def test_pep8_file_storage_test(self):
        '''
        Test that test/test_engine/test_file_storage.py
        conforms to PEP8
        '''
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ['tests/test_models/test_engine/test_file_storage.py'])
        mesg = "Found pep8 erros and warnings in test_file_storage.py"
        self.assertEqual(result.total_errors, 0, mesg)

    def test_module_documentation(self):
        ''' check module documentation '''
        doc = True
        try:
            len(file_storage.__doc__) >= 1
        except Exception:
            doc = False
        mesg = "No documentation found for {} module"
        self.assertEqual(
            True, doc, mesg.format(file_storage.__name__))

    def test_class_documentation(self):
        ''' check class FileStorage documentation '''
        doc = True
        try:
            len(FileStorage.__doc__) >= 1
        except Exception:
            doc = False
        mesg = "No documentation found for {} class"
        self.assertEqual(
            True, doc, mesg.format(file_storage.__name__))

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


class TestFileStorage(unittest.TestCase):
    ''' Test for FileStorage class '''
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

    def test__instance(self):
        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)

    def test__path_exists_variable(self):
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))

    def test__path_exists_variable(self):
        self.assertTrue(os.path.exists(FileStorage._FileStorage__objects))

    def test___file_path(self):
        self.assertEqual(FileStorage._FileStorage__file_path, self.path_file)

    def test__file_path_exists(self):
        storage = FileStorage()
        self.assertTrue(isinstance(storage._FileStorage__file_path, str))

    def test__objects_exists(self):
        storage = FileStorage()
        self.assertTrue(isinstance(storage._FileStorage__objects, dict))

    def test_all(self):
        storage = FileStorage()
        self.assertEqual(storage.all(), {})

    def test_new(self):
        base = BaseModel()
        storage = FileStorage()
        storage.new(base)
        self.assertNotEqual(storage.all(), {})

    def test_save_exists_file(self):
        base = BaseModel()
        base.save()
        self.assertTrue(os.path.exists(self.path_file))

    def test_save_test_content(self):
        base = BaseModel()
        base.name = 'test_storage'
        base.email = 'save@mail.com'
        base.save()
        self.assertTrue(os.path.exists(self.path_file))
        dict_to_load = {}
        with open(self.path_file, 'r') as reader:
                dict_to_load = json.loads(reader.read())
        self.assertDictEqual(
            base.to_dict(), dict_to_load['BaseModel.' + base.id])

    def test_reload(self):
        storage = FileStorage()
        base = BaseModel()
        base.name = 'test_storage'
        base.email = 'save@mail.com'
        base.save()
        FileStorage._FileStorage__objects = {}
        storage.reload()
        self.assertNotEqual(storage.all(), {})
