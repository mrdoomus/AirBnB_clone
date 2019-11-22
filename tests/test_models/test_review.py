#!/usr/bin/python3
''' Test for class Review '''
import unittest
from unittest import mock
from io import StringIO
import json
import pep8
import inspect
import datetime
import os
from models.engine.file_storage import FileStorage
from models import review
Review = review.Review


class TestReviewDoc(unittest.TestCase):
    '''
    calss to check documentation for Review class
    '''

    @classmethod
    def setUpClass(cls):
        ''' This method run before all test and
            find into Review class all functions.
            it store in a list of tuples
        '''
        cls.list_base_functions = inspect.getmembers(
            Review, inspect.isfunction)

    def test_pep8_review_class(self):
        ''' Test that models/review.py conforms to PEP8 '''
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found pep8 erros and warnings in review.py")

    def test_pep8_review_test(self):
        ''' Test that test/test_models/test_review.py conforms to PEP8 '''
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ['tests/test_models/test_review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found pep8 erros and warnings in test_review.py")

    def test_module_documentation(self):
        ''' check module documentation '''
        doc = True
        try:
            len(review.__doc__) >= 1
        except Exception:
            doc = False
        mesg = "No documentation found for {} module"
        self.assertEqual(
            True, doc, mesg.format(review.__name__))

    def test_class_documentation(self):
        ''' check class Review documentation '''
        doc = True
        try:
            len(Review.__doc__) >= 1
        except Exception:
            doc = False
        mesg = "No documentation found for {} class"
        self.assertEqual(
            True, doc, mesg.format(review.__name__))

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


class TestReview(unittest.TestCase):
    ''' Test for Review class '''
    @classmethod
    def setUpClass(cls):
        cls.path_file = 'file.json'
        cls.list_objects = [Review, Review,
                            Review, Review, Review]

    def setUp(self):
        FileStorage._FileStorage__objects = {}
        if os.path.exists(self.path_file):
            os.remove(self.path_file)

    def tearDown(self):
        FileStorage._FileStorage__objects = {}
        if os.path.exists(self.path_file):
            os.remove(self.path_file)

    def test_id_str(self):
        base = Review()

        self.assertIsInstance(base.id, str)

        self.assertIsInstance(base.id, str)

    def test___file_path_exists(self):
        self.assertEqual(FileStorage._FileStorage__file_path, self.path_file)

    def test__objects_exists(self):
        self.assertEqual(FileStorage._FileStorage__objects, {})

    def test_datetime(self):
        base = Review()
        self.assertIsInstance(base.created_at, datetime.datetime)
        self.assertIsInstance(base.updated_at, datetime.datetime)

    def test_create_object_simple(self):
        base = Review()
        base.name = "Holberton"
        base.my_number = 89
        self.assertTrue(base.id)
        self.assertTrue(base.name)
        self.assertTrue(base.my_number)

    def test_create_object_args(self):
        base = Review('name', 'Holberton')
        list_expected = list(base.__dict__.values())
        list_fail = list_expected + ['name', 'Holberton']
        self.assertNotEqual(list_expected, list_fail)

    def test_create_object_kwargs(self):
        base = Review(name='name', school='Holberton')
        self.assertTrue(base.name)
        self.assertTrue(base.school)
        self.assertEqual(base.name, 'name')
        self.assertEqual(base.school, 'Holberton')

    def test_create_object_simple_storage(self):
        base = Review()
        storage = FileStorage()
        dict_obects = storage.all()
        self.assertEqual(base, dict_obects['Review.' + base.id])

    def test_create_object_kwargs_storage(self):
        data = {'name': 'name', 'school': 'Holberton'}
        base = Review(**data)
        storage = FileStorage()
        self.assertDictEqual(storage.all(), {})

    def test__str__(self):
        base = Review()
        base.name = 'test'
        base.email = 'test@mail.com'
        str_rep = str(base)
        expected = "[{}] ({}) {}".format(
            base.__class__.__name__, base.id, base.__dict__)
        self.assertEqual(str_rep, expected)

    def test_str_output(self):
        base = Review()
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
        base = Review()
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
        base = Review()
        base.id = "123456"
        base.created_at = base.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'Review',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(base.to_dict(), tdict)

    def test_save_exists_file(self):
        base = Review()
        base.save()
        self.assertTrue(os.path.exists(self.path_file))

    def test_save_test_content(self):
        base = Review()
        base.name = 'test'
        base.email = 'test@mail.com'
        base.save()
        self.assertTrue(os.path.exists(self.path_file))
        dict_to_load = {}
        with open(self.path_file, 'r') as reader:
                dict_to_load = json.loads(reader.read())
        self.assertDictEqual(
            base.to_dict(), dict_to_load['Review.' + base.id])
