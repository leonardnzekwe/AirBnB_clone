#!/usr/bin/python3
"""
User class Test Module:
a class that inherits from BaseModel
"""


import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):
    """
    TestUser() class:
    a class that tests the User() class
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

    def test_instance_creation(self):
        """
        Test instance Creation:
        Test that User(BaseModel) instance is created properly
        """
        user_obj = User()
        self.assertIsInstance(user_obj, User)
        self.assertIsInstance(user_obj, BaseModel)
        self.assertTrue(hasattr(user_obj, "id"))
        self.assertTrue(hasattr(user_obj, "created_at"))
        self.assertTrue(hasattr(user_obj, "updated_at"))
        self.assertEqual(user_obj.email, "")
        self.assertEqual(user_obj.password, "")
        self.assertEqual(user_obj.first_name, "")
        self.assertEqual(user_obj.last_name, "")

    def test_attributes_assignment(self):
        """
        Test Attr Assignment:
        Test that class attributes are assigned correctly
        """
        user_obj = User(
            email="leo@email.com", password="password",
            first_name="Leo", last_name="Nze"
        )
        self.assertEqual(user_obj.email, "leo@email.com")
        self.assertEqual(user_obj.password, "password")
        self.assertEqual(user_obj.first_name, "Leo")
        self.assertEqual(user_obj.last_name, "Nze")

    def test_attributes_exist_with_value(self):
        """
        Test Attr Existence:
        Test that attributes exist in User instance
        """
        user_obj = User()
        self.assertTrue(hasattr(user_obj, "email"))
        self.assertTrue(hasattr(user_obj, "password"))
        self.assertTrue(hasattr(user_obj, "first_name"))
        self.assertTrue(hasattr(user_obj, "last_name"))

    def test_str_representation(self):
        """
        __str__() Test:
        Test __str__() representation is correct
        """
        user_obj = User()
        user_obj.email = "leo@email.com"
        user_obj.password = "password"
        user_obj_str = str(user_obj)
        self.assertIn("[User]", user_obj_str)
        self.assertIn("'id':", user_obj_str)
        self.assertIn("'email': 'leo@email.com'", user_obj_str)
        self.assertIn("'password': 'password'", user_obj_str)

    def test_save_method(self):
        """
        save() Test:
        Test save() method works correctly
        """
        user_obj = User()
        prev_updated_at = user_obj.updated_at
        user_obj.save()
        self.assertNotEqual(user_obj.updated_at, prev_updated_at)

    def test_to_dict_method(self):
        """
        to_dict() Test:
        Test to_dict() method works correctly
        """
        user_obj = User()
        user_obj.email = "leo@email.com"
        user_obj.first_name = ""
        user_obj.last_name = ""
        user_obj.password = ""
        user_dict = user_obj.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict["email"], "leo@email.com")
        self.assertEqual(user_dict["password"], "")
        self.assertEqual(user_dict["first_name"], "")
        self.assertEqual(user_dict["last_name"], "")
        self.assertEqual(user_dict["__class__"], "User")
        self.assertEqual(user_dict["id"], user_obj.id)
        self.assertEqual(
            user_dict["created_at"], user_obj.created_at.isoformat())
        self.assertEqual(
            user_dict["updated_at"], user_obj.updated_at.isoformat())

    def test_created_at_and_updated_at_are_datetime_objects(self):
        """
        Is Datetime Objects Test:
        Test created_at & updated_at are datetime objects
        """
        user_obj = User()
        self.assertIsInstance(user_obj.created_at, datetime)
        self.assertIsInstance(user_obj.updated_at, datetime)

    def test_different_user_instances_have_different_ids(self):
        """
        Instance Id Test:
        Test different User instance have different id's
        """
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_class_inheritance(self):
        """
        Class Test:
        Test if User() or its instance inherits from BaseModel
        """
        user_obj = User()
        self.assertIsInstance(user_obj, BaseModel)
        self.assertIsInstance(User(), BaseModel)

    def test_method_inherited(self):
        """
        Method Test:
        Test inherited methods
        """
        user_obj = User()
        self.assertTrue(hasattr(user_obj, "save"))
        self.assertTrue(hasattr(user_obj, "to_dict"))

    def test_documentations(self):
        """
        Documentation Test:
        Test if there is a doc in module, class and methods.
        """
        from models import user

        self.assertIsNotNone(user.__doc__)
        self.assertGreater(len(user.__doc__), 5)

        self.assertIsNotNone(User.__doc__)
        self.assertGreater(len(User.__doc__), 5)


if __name__ == "__main__":
    unittest.main()
