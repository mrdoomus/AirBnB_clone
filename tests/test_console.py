#!/usr/bin/python3
''' Test for class HBNBCommand '''
import unittest
from unittest import mock
import sys
from io import StringIO
import pep8
import inspect
import console
import os
from models import *
HBNBCommand = console.HBNBCommand


class TestHBNBCommandDoc(unittest.TestCase):
    '''
    calss to check documentation for HBNBCommand class
    '''

    @classmethod
    def setUpClass(cls):
        ''' This method run before all test and
            find into HBNBCommand class all functions.
            it store in a list of tuples
        '''
        cls.list_base_functions = inspect.getmembers(
            HBNBCommand, inspect.isfunction)

    def test_pep8_console_class(self):
        ''' Test that console.py conforms to PEP8 '''
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found pep8 erros and warnings in console.py")

    def test_pep8_console_test(self):
        ''' Test that tests/test_console.py conforms to PEP8 '''
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found pep8 erros and warnings in test_console.py")

    def test_module_documentation(self):
        ''' check module documentation '''
        doc = True
        try:
            len(console.__doc__) >= 1
        except Exception:
            doc = False
        mesg = "No documentation found for {} module"
        self.assertEqual(
            True, doc, mesg.format(console.__name__))

    def test_class_documentation(self):
        ''' check class HBNBCommand documentation '''
        doc = True
        try:
            len(HBNBCommand.__doc__) >= 1
        except Exception:
            doc = False
        mesg = "No documentation found for {} class"
        self.assertEqual(
            True, doc, mesg.format(HBNBCommand.__name__))

    def test_functions(self):
        ''' check documentation for every function '''
        for item in self.list_base_functions:
            function = item[1]
            if str(function).find("function Cmd") != -1:
                continue
            doc = True
            try:
                len(function.__doc__) >= 1
            except Exception:
                doc = False
            mesg = "No documentation found for < def {} > function"
            self.assertEqual(
                True, doc, mesg.format(function.__name__))


class TestHBNBCommand(unittest.TestCase):
    ''' Test for HBNBCommand class '''
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

    def with_mock(self, cmd, expected):

        with mock.patch('sys.stdout', new=StringIO()) as std_out:
            HBNBCommand().onecmd(cmd)
            output = std_out.getvalue()
            self.assertEqual(output.strip(), expected.strip())

    def test_console_help(self):
        expected = ("Documented commands (type help <topic>):\n"
                    "========================================\n"
                    "EOF  all  create  destroy  help  quit  show  update\n")
        self.with_mock(cmd="help", expected=expected)

    def test_exit(self):
        self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF(self):
        self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test_create(self):
        self.with_mock(cmd="create", expected="** class name missing **")
        self.with_mock(cmd="create MyModel",
                       expected="** class doesn't exist **")
        self.with_mock(cmd="create MyModel",
                       expected="** class doesn't exist **")

    def test_show(self):
        self.with_mock(cmd="show", expected="** class name missing **")
        self.with_mock(cmd="show MyModel",
                       expected="** class doesn't exist **")
        self.with_mock(cmd="show BaseModel",
                       expected="** instance id missing **")

    def test_destroy(self):
        self.with_mock(cmd="destroy", expected="** class name missing **")
        self.with_mock(cmd="destroy MyModel",
                       expected="** class doesn't exist **")
        self.with_mock(cmd="destroy BaseModel",
                       expected="** instance id missing **")
        self.with_mock(cmd="destroy BaseModel 121212",
                       expected="** no instance found **")

    def test_all(self):
        self.with_mock(cmd="all MyModel",
                       expected="** class doesn't exist **")

    def test_update(self):
        self.with_mock(cmd="update", expected="** class name missing **")
        self.with_mock(cmd="update MyModel",
                       expected="** class doesn't exist **")
        self.with_mock(cmd="update BaseModel",
                       expected="** instance id missing **")
        self.with_mock(cmd="update BaseModel 121212",
                       expected="** no instance found **")

    def test_create_object(self):
        output = ""
        with mock.patch('sys.stdout', new=StringIO()) as std_out:
            FileStorage._FileStorage__objects = {}
            storage = FileStorage()
            HBNBCommand().onecmd("create Amenity")
            output = std_out.getvalue()
            list_obj = list(storage.all().values())
            self.assertEqual(output.strip(), list_obj[0].id)

        with mock.patch('sys.stdout', new=StringIO()) as std_out:
            FileStorage._FileStorage__objects = {}
            storage = FileStorage()
            HBNBCommand().onecmd("create BaseModel")
            output = std_out.getvalue()
            list_obj = list(storage.all().values())
            self.assertEqual(output.strip(), list_obj[0].id)
        with mock.patch('sys.stdout', new=StringIO()) as std_out:
            FileStorage._FileStorage__objects = {}
            storage = FileStorage()
            HBNBCommand().onecmd("create City")
            output = std_out.getvalue()
            list_obj = list(storage.all().values())
            self.assertEqual(output.strip(), list_obj[0].id)
        with mock.patch('sys.stdout', new=StringIO()) as std_out:
            FileStorage._FileStorage__objects = {}
            storage = FileStorage()
            HBNBCommand().onecmd("create Place")
            output = std_out.getvalue()
            list_obj = list(storage.all().values())
            self.assertEqual(output.strip(), list_obj[0].id)
        with mock.patch('sys.stdout', new=StringIO()) as std_out:
            FileStorage._FileStorage__objects = {}
            storage = FileStorage()
            HBNBCommand().onecmd("create Review")
            output = std_out.getvalue()
            list_obj = list(storage.all().values())
            self.assertEqual(output.strip(), list_obj[0].id)
        with mock.patch('sys.stdout', new=StringIO()) as std_out:
            FileStorage._FileStorage__objects = {}
            storage = FileStorage()
            HBNBCommand().onecmd("create State")
            output = std_out.getvalue()
            list_obj = list(storage.all().values())
            self.assertEqual(output.strip(), list_obj[0].id)
        with mock.patch('sys.stdout', new=StringIO()) as std_out:
            FileStorage._FileStorage__objects = {}
            storage = FileStorage()
            HBNBCommand().onecmd("create User")
            output = std_out.getvalue()
            list_obj = list(storage.all().values())
            self.assertEqual(output.strip(), list_obj[0].id)

    def test_show_object(self):

        with mock.patch('sys.stdout', new=StringIO()) as std_out:
            base = base_model.BaseModel()
            HBNBCommand().onecmd("show BaseModel {}".format(base.id))
            output = std_out.getvalue()
            self.assertEqual(output.strip(), str(base))
        with mock.patch('sys.stdout', new=StringIO()) as std_out:
            base = city.City()
            HBNBCommand().onecmd("show City {}".format(base.id))
            output = std_out.getvalue()
            self.assertEqual(output.strip(), str(base))
        with mock.patch('sys.stdout', new=StringIO()) as std_out:
            base = place.Place()
            HBNBCommand().onecmd("show Place {}".format(base.id))
            output = std_out.getvalue()
            self.assertEqual(output.strip(), str(base))
        with mock.patch('sys.stdout', new=StringIO()) as std_out:
            base = review.Review()
            HBNBCommand().onecmd("show Review {}".format(base.id))
            output = std_out.getvalue()
            self.assertEqual(output.strip(), str(base))
        with mock.patch('sys.stdout', new=StringIO()) as std_out:
            base = state.State()
            HBNBCommand().onecmd("show State {}".format(base.id))
            output = std_out.getvalue()
            self.assertEqual(output.strip(), str(base))
        with mock.patch('sys.stdout', new=StringIO()) as std_out:
            base = user.User()
            HBNBCommand().onecmd("show User {}".format(base.id))
            output = std_out.getvalue()
            self.assertEqual(output.strip(), str(base))

    def test_help_show(self):
        """Test the help command"""
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
        output = f.getvalue().strip()
        expected1 = "Prints the string representation of an instance."
        expected2 = "        Use: show [CLASS] [ID]"
        expected3 = "        Ex: show BaseModel 1234-1234-1234."
        self.assertIn(expected1, output)
        self.assertIn(expected2, output)
        self.assertIn(expected3, output)

    def test_help_quit(self):
        """Test the help quit command"""
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
        output = f.getvalue().strip()
        expected1 = "Quit command to exit the program"
        self.assertIn(expected1, output)

    def test_all(self):
        """Test the all command"""
        FileStorage._FileStorage__objects = {}
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
        output1 = f.getvalue().strip()
        self.assertEqual("[]", output1)
        base = user.User()
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all User")
        output3 = f.getvalue().strip()
        self.assertIn("[User]", output3)
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all Not Class")
        output3 = f.getvalue().strip()
        self.assertIn("** class doesn't exist **", output3)

    def test_all_string(self):
        """Test the all command"""
        storage.__objects = {}
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
        output1 = f.getvalue().strip()

        self.assertEqual("[]", output1)
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.all()")
            HBNBCommand().onecmd("create User")
        output2 = f.getvalue().strip()

        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.all()")
        output3 = f.getvalue().strip()
        self.assertIn("'created_at': datetime.datetime(", output3)
        self.assertIn("'updated_at': datetime.datetime(", output3)
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.all()")
        output3 = f.getvalue().strip()
        self.assertIn("'created_at': datetime.datetime(", output3)
        self.assertIn("'updated_at': datetime.datetime(", output3)

    def test_create(self):
        """Test the create command"""
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        output1 = f.getvalue().strip()
        with mock.patch('sys.stdout', new=StringIO()) as f:
            my_input = str("show User " + output1)
            HBNBCommand().onecmd(my_input)
        output2 = f.getvalue().strip()
        self.assertIn(str("[User] (" + output1 + ")"), output2)
        self.assertIn("'created_at': datetime.datetime(", output2)
        self.assertIn("'updated_at': datetime.datetime(", output2)
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
        output1 = f.getvalue().strip()
        with mock.patch('sys.stdout', new=StringIO()) as f:
            my_input = str("show City " + output1)
            HBNBCommand().onecmd(my_input)
        output2 = f.getvalue().strip()
        self.assertIn(str("[City] (" + output1 + ")"), output2)
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
        output1 = f.getvalue().strip()
        with mock.patch('sys.stdout', new=StringIO()) as f:
            my_input = str("show State " + output1)
            HBNBCommand().onecmd(my_input)
        output2 = f.getvalue().strip()
        self.assertIn(str("[State] (" + output1 + ")"), output2)
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
        output1 = f.getvalue().strip()
        with mock.patch('sys.stdout', new=StringIO()) as f:
            my_input = str("show Place " + output1)
            HBNBCommand().onecmd(my_input)
        output2 = f.getvalue().strip()
        self.assertIn(str("[Place] (" + output1 + ")"), output2)
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
        output1 = f.getvalue().strip()
        with mock.patch('sys.stdout', new=StringIO()) as f:
            my_input = str("show Amenity " + output1)
            HBNBCommand().onecmd(my_input)
        output2 = f.getvalue().strip()
        self.assertIn(str("[Amenity] (" + output1 + ")"), output2)
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
        output1 = f.getvalue().strip()
        with mock.patch('sys.stdout', new=StringIO()) as f:
            my_input = str("show Review " + output1)
            HBNBCommand().onecmd(my_input)
        output2 = f.getvalue().strip()
        self.assertIn(str("[Review] (" + output1 + ")"), output2)

    def test_show2(self):
        """Test the create command"""
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        output1 = f.getvalue().strip()
        with mock.patch('sys.stdout', new=StringIO()) as f:
            my_input = str("User.show(" + output1 + ")")
            HBNBCommand().onecmd(my_input)
        output2 = f.getvalue().strip()
        self.assertIn(str("[User] (" + output1 + ")"), output2)
        self.assertIn("'created_at': datetime.datetime(", output2)
        self.assertIn("'updated_at': datetime.datetime(", output2)
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Test')
        output2 = f.getvalue().strip()
        self.assertEqual("** class doesn't exist **", output2)

    def test_count(self):
        """Test the count command"""
        FileStorage._FileStorage__objects = {}
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        output1 = f.getvalue().strip()
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('User.count()')
        output2 = f.getvalue().strip()
        self.assertEqual('1', output2)
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.count()")
        output2 = f.getvalue().strip()
        self.assertEqual('2', output2)

    def test_show_errors(self):
        """Test the show command error messages"""
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        output1 = f.getvalue().strip()
        with mock.patch('sys.stdout', new=StringIO()) as f:
            my_input = str("show")
            HBNBCommand().onecmd(my_input)
        output2 = f.getvalue().strip()
        self.assertEqual("** class name missing **", output2)
        with mock.patch('sys.stdout', new=StringIO()) as f:
            my_input = str("show User")
            HBNBCommand().onecmd(my_input)
        output3 = f.getvalue().strip()
        self.assertIn("** instance id missing **", output3)
        with mock.patch('sys.stdout', new=StringIO()) as f:
            my_input = str("show User 89698")
            HBNBCommand().onecmd(my_input)
        output4 = f.getvalue().strip()
        self.assertIn("** no instance found **", output4)

    def test_destroy(self):
        """Test the destroy command"""
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        output1 = f.getvalue().strip()
        with mock.patch('sys.stdout', new=StringIO()) as f:
            my_input = str("destroy User " + output1)
            HBNBCommand().onecmd(my_input)
        with mock.patch('sys.stdout', new=StringIO()) as f:
            my_input = str("show User " + output1)
            HBNBCommand().onecmd(my_input)
        output2 = f.getvalue().strip()
        self.assertIn("** no instance found **", output2)

    def test_destroy2(self):
        """Test the destroy command"""
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        output1 = f.getvalue().strip()
        with mock.patch('sys.stdout', new=StringIO()) as f:
            my_input = str("User.destroy(" + output1 + ")")
            HBNBCommand().onecmd(my_input)
        with mock.patch('sys.stdout', new=StringIO()) as f:
            my_input = str("show User " + output1)
            HBNBCommand().onecmd(my_input)
        output2 = f.getvalue().strip()
        self.assertIn("** no instance found **", output2)

    def test_destroy_errors(self):
        """Test the destroy command error messages"""
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        output1 = f.getvalue().strip()
        with mock.patch('sys.stdout', new=StringIO()) as f:
            my_input = str("destroy")
            HBNBCommand().onecmd(my_input)
        output2 = f.getvalue().strip()
        self.assertEqual("** class name missing **", output2)
        with mock.patch('sys.stdout', new=StringIO()) as f:
            my_input = str("destroy User")
            HBNBCommand().onecmd(my_input)
        output3 = f.getvalue().strip()
        self.assertIn("** instance id missing **", output3)
        with mock.patch('sys.stdout', new=StringIO()) as f:
            my_input = str("destroy User 89698")
            HBNBCommand().onecmd(my_input)
        output4 = f.getvalue().strip()
        self.assertIn("** no instance found **", output4)

    def test_update(self):
        """Test the create command"""
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        output1 = f.getvalue().strip()
        with mock.patch('sys.stdout', new=StringIO()) as f:
            my_input1 = str("update User " + output1 + 'name "test this name"')
            HBNBCommand().onecmd(my_input1)
        with mock.patch('sys.stdout', new=StringIO()) as f:
            my_input2 = str("show User " + output1)
            HBNBCommand().onecmd(my_input2)
        output2 = f.getvalue().strip()
        self.assertIn(str("[User] (" + output1 + ")"), output2)
        self.assertIn("'created_at': datetime.datetime(", output2)
        self.assertIn("'updated_at': datetime.datetime(", output2)

    def test_update2(self):
        """Test the create command"""
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        output1 = f.getvalue().strip()
        with mock.patch('sys.stdout', new=StringIO()) as f:
            my_input1 = str("User.update(" + output1 + ', "name",'
                                                       '"test this name")')
            HBNBCommand().onecmd(my_input1)
        with mock.patch('sys.stdout', new=StringIO()) as f:
            my_input2 = str("show User " + output1)
            HBNBCommand().onecmd(my_input2)
        output2 = f.getvalue().strip()
        self.assertIn(str("[User] (" + output1 + ")"), output2)
        self.assertIn("'created_at': datetime.datetime(", output2)
        self.assertIn("'updated_at': datetime.datetime(", output2)

    def test_update_errors(self):
        """Test the destroy command error messages"""
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        output1 = f.getvalue().strip()
        with mock.patch('sys.stdout', new=StringIO()) as f:
            my_input = str("update")
            HBNBCommand().onecmd(my_input)
        output2 = f.getvalue().strip()
        self.assertEqual("** class name missing **", output2)
        with mock.patch('sys.stdout', new=StringIO()) as f:
            my_input = str("update User")
            HBNBCommand().onecmd(my_input)
        output3 = f.getvalue().strip()
        self.assertIn("** instance id missing **", output3)
        with mock.patch('sys.stdout', new=StringIO()) as f:
            my_input = str("update User 89698")
            HBNBCommand().onecmd(my_input)
        output4 = f.getvalue().strip()
        self.assertIn("** no instance found **", output4)
