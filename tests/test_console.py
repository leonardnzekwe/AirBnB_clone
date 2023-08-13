#!/usr/bin/python3
"""
Test module for HBNBCommand class:
a class that contains the entry point of the command interpreter.
"""

import os
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.engine.file_storage import FileStorage
from models.user import User


class TestHBNBCommand(unittest.TestCase):
    """
    TestHBNBCommand class:
    Test suite for the HBNBCommand class in console.py
    """

    @classmethod
    def setUpClass(cls):
        """
        setUp() instance method:
        Create a new instance of FileStorage before each test
        """
        cls.file_storage = FileStorage()

    @classmethod
    def tearDownClass(cls):
        """
        tearDown() instance method:
        Clean up by removing the test JSON file if it exists after each test
        """
        if os.path.exists(cls.file_storage._FileStorage__file_path):
            os.remove(cls.file_storage._FileStorage__file_path)

    def setUp(self):
        """
        setUp() instance method:
        Create an instance of HBNBCommand before each test
        """
        self.console = HBNBCommand()
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("create User")
            self.id = f.getvalue().strip()

    def tearDown(self):
        """
        tearDown() instance method:
        Clean up by removing the reference to the console instance
        after each test
        """
        self.console = None

    def test_quit(self):
        """
        Test quit command:
        Ensure the quit command exits the program
        """
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("quit"))
            output = f.getvalue().strip()
            self.assertEqual(output, "")

    def test_EOF(self):
        """
        Test EOF command:
        Ensure the EOF command exits the program
        """
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("EOF"))
            output = f.getvalue().strip()
            self.assertEqual(output, "")

    def test_emptyline(self):
        """
        Test emptyline method:
        Ensure that an empty line does nothing
        """
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("")
            output = f.getvalue().strip()
            self.assertEqual(output, "")

    def test_create_missing_class_name(self):
        """
        Test create method with missing class name:
        Ensure that create displays an error message for missing class name
        """
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("create")
            expected_output = "** class name missing **"
            output = f.getvalue().strip()
            self.assertEqual(output, expected_output)

    def test_create_invalid_class(self):
        """
        Test create method with invalid class name:
        Ensure that create displays an error message for invalid class name
        """
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("create InvalidClass")
            expected_output = "** class doesn't exist **"
            output = f.getvalue().strip()
            self.assertEqual(output, expected_output)

    def test_all_invalid_class(self):
        """
        Test all method with invalid class name:
        Ensure that all displays an error message for invalid class name
        """
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("all InvalidClass")
            expected_output = "** class doesn't exist **"
            output = f.getvalue().strip()
            self.assertEqual(output, expected_output)

    def test_all_with_class(self):
        """
        Test all method with a valid class name:
        Ensure that all displays instances of the specified class
        """
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("all User")
            output = f.getvalue().strip()
            self.assertTrue(len(output) > 0)

    def test_all_without_class(self):
        """
        Test all method without a class name:
        Ensure that all displays instances of all classes
        """
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("all")
            output = f.getvalue().strip()
            self.assertTrue(len(output) > 0)

    def test_destroy_missing_class_name(self):
        """
        Test destroy method with missing class name:
        Ensure that destroy displays an error message for missing class name
        """
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("destroy")
            expected_output = "** class name missing **"
            output = f.getvalue().strip()
            self.assertEqual(output, expected_output)

    def test_destroy_invalid_class(self):
        """
        Test destroy method with invalid class name:
        Ensure that destroy displays an error message for invalid class name
        """
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("destroy InvalidClass")
            expected_output = "** class doesn't exist **"
            output = f.getvalue().strip()
            self.assertEqual(output, expected_output)

    def test_destroy_missing_instance_id(self):
        """
        Test destroy method with missing instance ID:
        Ensure that destroy displays an error message for missing instance ID
        """
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("destroy User")
            expected_output = "** instance id missing **"
            output = f.getvalue().strip()
            self.assertEqual(output, expected_output)

    def test_destroy_invalid_instance_id(self):
        """
        Test destroy method with invalid instance ID:
        Ensure that destroy displays an error message for invalid instance ID
        """
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("destroy User invalid_id")
            expected_output = "** no instance found **"
            output = f.getvalue().strip()
            self.assertEqual(output, expected_output)

    def test_show_missing_class_name(self):
        """
        Test show method with missing class name:
        Ensure that show displays an error message for missing class name
        """
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("show")
            expected_output = "** class name missing **"
            output = f.getvalue().strip()
            self.assertEqual(output, expected_output)

    def test_show_invalid_class(self):
        """
        Test show method with invalid class name:
        Ensure that show displays an error message for invalid class name
        """
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("show InvalidClass")
            expected_output = "** class doesn't exist **"
            output = f.getvalue().strip()
            self.assertEqual(output, expected_output)

    def test_show_missing_instance_id(self):
        """
        Test show method with missing instance ID:
        Ensure that show displays an error message for missing instance ID
        """
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("show User")
            expected_output = "** instance id missing **"
            output = f.getvalue().strip()
            self.assertEqual(output, expected_output)

    def test_show_invalid_instance_id(self):
        """
        Test show method with invalid instance ID:
        Ensure that show displays an error message for invalid instance ID
        """
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("show User invalid_id")
            expected_output = "** no instance found **"
            output = f.getvalue().strip()
            self.assertEqual(output, expected_output)

    def test_update_missing_class_name(self):
        """
        Test update method with missing class name:
        Ensure that update displays an error message for missing class name
        """
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("update")
            expected_output = "** class name missing **"
            output = f.getvalue().strip()
            self.assertEqual(output, expected_output)

    def test_update_invalid_class(self):
        """
        Test update method with invalid class name:
        Ensure that update displays an error message for invalid class name
        """
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("update InvalidClass")
            expected_output = "** class doesn't exist **"
            output = f.getvalue().strip()
            self.assertEqual(output, expected_output)

    def test_update_missing_instance_id(self):
        """
        Test update method with missing instance ID:
        Ensure that update displays an error message for missing instance ID
        """
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("update User")
            expected_output = "** instance id missing **"
            output = f.getvalue().strip()
            self.assertEqual(output, expected_output)

    def test_update_invalid_instance_id(self):
        """
        Test update method with invalid instance ID:
        Ensure that update displays an error message for invalid instance ID
        """
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("update User invalid_id")
            expected_output = "** no instance found **"
            output = f.getvalue().strip()
            self.assertEqual(output, expected_output)

    def test_update_missing_attribute_name(self):
        """
        Test update method with missing attribute name:
        Ensure that update displays an error message for missing attribute name
        """
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd(f"update User {self.id}")
            expected_output = "** attribute name missing **"
            output = f.getvalue().strip()
            self.assertEqual(output, expected_output)

    def test_update_missing_value(self):
        """
        Test update method with missing value:
        Ensure that update displays an error message for missing value
        """
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd(f'update User {self.id} "name"')
            expected_output = "** value missing **"
            output = f.getvalue().strip()
            self.assertEqual(output, expected_output)

    def test_count_invalid_class(self):
        """
        Test count method with invalid class name:
        Ensure that count displays an error message for invalid class name
        """
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("count InvalidClass")
            expected_output = "** class doesn't exist **"
            output = f.getvalue().strip()
            self.assertEqual(output, expected_output)

    def test_count_with_class(self):
        """
        Test count method with a valid class name:
        Ensure that count displays the number of instances
        of the specified class
        """
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("count User")
            output = f.getvalue().strip()
            self.assertTrue(output.isdigit())

    def test_count_without_class(self):
        """
        Test count method without a class name:
        Ensure that count displays the total number of instances
        across all classes
        """
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("count")
            output = f.getvalue().strip()
            self.assertTrue(output.isdigit())

    def test_create_valid_class(self):
        """
        Test create method with valid class name:
        Ensure that create correctly creates an instance of a valid class
        """
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("create State")
            instance_id = f.getvalue().strip()
            expected_output = f"State.{self.file_storage.all()}"
            self.assertIn(instance_id, expected_output)

    def test_show_valid_instance(self):
        """
        Test show method with valid instance ID:
        Ensure that show displays the correct instance details
        """
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd(f"show User {self.id}")
            output = f.getvalue().strip()
            self.assertTrue(self.id in output)

    def test_destroy_valid_instance(self):
        """
        Test destroy method with valid instance ID:
        Ensure that destroy removes the specified instance
        """
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd(f"destroy User {self.id}")
            self.assertTrue(self.id not in self.file_storage.all())

    def test_update_valid_instance(self):
        """
        Test update method with valid instance ID and attributes:
        Ensure that update updates the specified instance attributes
        """
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd(f'update User {self.id} name "new_name"')
            updated_instance = self.file_storage.all()[f"User.{self.id}"]
            self.assertEqual(updated_instance.name, "new_name")

    def test_all_without_class(self):
        """
        Test all method without a class name:
        Ensure that all displays instances of all classes
        """
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("all")
            output = f.getvalue().strip()
            self.assertTrue(len(output) > 0)

    def test_all_with_class(self):
        """
        Test all method with a valid class name:
        Ensure that all displays instances of the specified class
        """
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("all User")
            output = f.getvalue().strip()
            self.assertTrue(len(output) > 0)

    def test_all_with_class_method(self):
        """
        Test <class_name>.all() method:
        Ensure that <class_name>.all()
        displays instances of the specified class
        """
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("create User")
            self.console.precmd("User.all()")
            output = f.getvalue().strip()
            self.assertTrue(len(output) > 0)

    def test_count_without_class(self):
        """
        Test count method without a class name:
        Ensure that count correctly counts the total number of instances
        across all classes
        """
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("count")
            count = int(f.getvalue().strip())
            expected_count = len(self.file_storage.all())
            self.assertEqual(count, expected_count)

    def test_count_with_class(self):
        """
        Test count method with a valid class name:
        Ensure that count correctly counts the instances of a valid class
        """
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("count User")
            count = int(f.getvalue().strip())
            expected_count = sum(
                1 for key in self.file_storage.all() if "User" in key
            )
            self.assertEqual(count, expected_count)

    def test_count_with_class_method(self):
        """
        Test <class_name>.count() method:
        Ensure that <class_name>.count()
        correctly counts the instances of a class
        """
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("User.count()")
            count = f.getvalue().strip()
            expected_count = sum(
                1 for key in self.file_storage.all() if "User" in key
            )
            self.assertIn(count, str(expected_count))

    def test_destroy_valid_instance(self):
        """
        Test destroy method with valid instance ID:
        Ensure that destroy removes the specified instance
        """
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("create State")
            idn = f.getvalue().strip()
            self.console.onecmd(f"destroy User {idn}")
            self.assertTrue(idn not in self.file_storage.all())

    def test_destroy_with_class_method(self):
        """
        Test <class_name>.destroy() method:
        Ensure that <class_name>.destroy() removes the specified instance
        """
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("create State")
            idn = f.getvalue().strip
            self.console.onecmd(f"User.destroy('{idn}')")
            self.assertNotIn(self.id, self.file_storage.all())

    def test_show_valid_instance(self):
        """
        Test show method with valid instance ID:
        Ensure that show displays the correct instance details
        """
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd(f"show User {self.id}")
            output = f.getvalue().strip()
            self.assertTrue(self.id in output)

    def test_show_with_class_method(self):
        """
        Test <class_name>.show() method:
        Ensure that <class_name>.show()
        displays the correct instance details
        """
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd(f"User.show('{self.id}')")
            output = f.getvalue().strip()
            self.assertIsNotNone(output)

    def test_update_valid_instance(self):
        """
        Test update method with valid instance ID and attributes:
        Ensure that update updates the specified instance attributes
        """
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd(f'update User {self.id} name "new_name"')
            updated_instance = self.file_storage.all()[f"User.{self.id}"]
            self.assertEqual(updated_instance.name, "new_name")

    def test_update_with_class_method(self):
        """
        Test <class_name>.update() method:
        Ensure that <class_name>.update()
        updates the specified instance attributes
        """
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd(
                f'User.update("{self.id}", "first_name", "new_name")'
            )
            updated_instance = self.file_storage.all()[f"User.{self.id}"]
            self.assertIn(updated_instance.first_name, "new_name")

    def test_update_with_dictionary(self):
        """
        Test update method with a dict rep:
        Ensure that update updates the specified
        instance attributes using a dictionary
        """
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd(
                f'update User {self.id} {{"first_name": "new_name"}}'
            )
            updated_instance = self.file_storage.all()[f"User.{self.id}"]
            self.assertIn(updated_instance.first_name, "new_name")

    def test_documentations(self):
        """
        Documentation Test:
        Test if there is a doc in module, class and methods.
        """
        import console

        self.assertIsNotNone(console.__doc__)
        self.assertGreater(len(console.__doc__), 5)

        self.assertIsNotNone(HBNBCommand.__doc__)
        self.assertGreater(len(HBNBCommand.__doc__), 5)

        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertGreater(len(HBNBCommand.do_all.__doc__), 5)

        self.assertIsNotNone(HBNBCommand.do_count.__doc__)
        self.assertGreater(len(HBNBCommand.do_count.__doc__), 5)

        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertGreater(len(HBNBCommand.do_create.__doc__), 5)

        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertGreater(len(HBNBCommand.do_destroy.__doc__), 5)

        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertGreater(len(HBNBCommand.do_EOF.__doc__), 5)

        self.assertIsNotNone(HBNBCommand.do_help.__doc__)
        self.assertGreater(len(HBNBCommand.do_help.__doc__), 5)

        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertGreater(len(HBNBCommand.do_quit.__doc__), 5)

        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertGreater(len(HBNBCommand.do_update.__doc__), 5)

        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertGreater(len(HBNBCommand.emptyline.__doc__), 5)

        self.assertIsNotNone(HBNBCommand.process_args.__doc__)
        self.assertGreater(len(HBNBCommand.process_args.__doc__), 5)


if __name__ == "__main__":
    unittest.main()
