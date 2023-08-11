#!/usr/bin/python3
"""
State class Test Module:
a class that inherits from BaseModel
"""


import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.state import State
from datetime import datetime


class TestState(unittest.TestCase):
    """
    TestState() class:
    a class that tests the State() class
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
        Test that State(BaseModel) instance is created properly
        """
        state_obj = State()
        self.assertIsInstance(state_obj, State)
        self.assertIsInstance(state_obj, BaseModel)
        self.assertTrue(hasattr(state_obj, "id"))
        self.assertTrue(hasattr(state_obj, "created_at"))
        self.assertTrue(hasattr(state_obj, "updated_at"))
        self.assertEqual(state_obj.name, "")

    def test_attributes_assignment(self):
        """
        Test Attr Assignment:
        Test that class attributes are assigned correctly
        """
        state_obj = State(name="Enugu")
        self.assertEqual(state_obj.name, "Enugu")

    def test_attributes_exist_with_value(self):
        """
        Test Attr Existence:
        Test that attributes exist in User instance
        """
        state_obj = State()
        self.assertTrue(hasattr(state_obj, "name"))

    def test_str_representation(self):
        """
        __str__() Test:
        Test __str__() representation is correct
        """
        state_obj = State()
        state_obj.name = "Enugu"
        state_obj_str = str(state_obj)
        self.assertIn("[State]", state_obj_str)
        self.assertIn("'id':", state_obj_str)
        self.assertIn("'name': 'Enugu'", state_obj_str)

    def test_save_method(self):
        """
        save() Test:
        Test save() method works correctly
        """
        state_obj = State()
        prev_updated_at = state_obj.updated_at
        state_obj.save()
        self.assertNotEqual(state_obj.updated_at, prev_updated_at)

    def test_to_dict_method(self):
        """
        to_dict() Test:
        Test to_dict() method works correctly
        """
        state_obj = State()
        state_obj.name = "Enugu"
        state_dict = state_obj.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict["name"], "Enugu")
        self.assertEqual(state_dict["__class__"], "State")
        self.assertEqual(state_dict["id"], state_obj.id)
        self.assertEqual(
            state_dict["created_at"], state_obj.created_at.isoformat())
        self.assertEqual(
            state_dict["updated_at"], state_obj.updated_at.isoformat())

    def test_created_at_and_updated_at_are_datetime_objects(self):
        """
        Is Datetime Objects Test:
        Test created_at & updated_at are datetime objects
        """
        state_obj = State()
        self.assertIsInstance(state_obj.created_at, datetime)
        self.assertIsInstance(state_obj.updated_at, datetime)

    def test_different_state_instances_have_different_ids(self):
        """
        Instance Id Test:
        Test different State instance have different id's
        """
        state1 = State()
        state2 = State()
        self.assertNotEqual(state1.id, state2.id)

    def test_class_inheritance(self):
        """
        Class Test:
        Test if State() or its instance inherits from BaseModel
        """
        state_obj = State()
        self.assertIsInstance(state_obj, BaseModel)
        self.assertIsInstance(State(), BaseModel)

    def test_method_inherited(self):
        """
        Method Test:
        Test inherited methods
        """
        state_obj = State()
        self.assertTrue(hasattr(state_obj, "save"))
        self.assertTrue(hasattr(state_obj, "to_dict"))

    def test_documentations(self):
        """
        Documentation Test:
        Test if there is a doc in module, class and methods.
        """
        from models import state

        self.assertIsNotNone(state.__doc__)
        self.assertGreater(len(state.__doc__), 5)

        self.assertIsNotNone(State.__doc__)
        self.assertGreater(len(State.__doc__), 5)


if __name__ == "__main__":
    unittest.main()
