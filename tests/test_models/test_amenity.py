#!/usr/bin/python3
"""
Amenity class Test Module:
a class that inherits from BaseModel
"""


import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """
    TestAmenity() class:
    a class that tests the Amenity() class
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
        Test that Amenity(BaseModel) instance is created properly
        """
        amenity_obj = Amenity()
        self.assertIsInstance(amenity_obj, Amenity)
        self.assertIsInstance(amenity_obj, BaseModel)
        self.assertTrue(hasattr(amenity_obj, "id"))
        self.assertTrue(hasattr(amenity_obj, "created_at"))
        self.assertTrue(hasattr(amenity_obj, "updated_at"))
        self.assertEqual(amenity_obj.name, "")

    def test_attributes_assignment(self):
        """
        Test Attr Assignment:
        Test that class attributes are assigned correctly
        """
        amenity_obj = Amenity(name="Luxury")
        self.assertEqual(amenity_obj.name, "Luxury")

    def test_attributes_exist_with_value(self):
        """
        Test Attr Existence:
        Test that attributes exist in User instance
        """
        amenity_obj = Amenity()
        self.assertTrue(hasattr(amenity_obj, "name"))

    def test_str_representation(self):
        """
        __str__() Test:
        Test __str__() representation is correct
        """
        amenity_obj = Amenity()
        amenity_obj.name = "Luxury"
        amenity_obj_str = str(amenity_obj)
        self.assertIn("[Amenity]", amenity_obj_str)
        self.assertIn("'id':", amenity_obj_str)
        self.assertIn("'name': 'Luxury'", amenity_obj_str)

    def test_save_method(self):
        """
        save() Test:
        Test save() method works correctly
        """
        amenity_obj = Amenity()
        prev_updated_at = amenity_obj.updated_at
        amenity_obj.save()
        self.assertNotEqual(amenity_obj.updated_at, prev_updated_at)

    def test_to_dict_method(self):
        """
        to_dict() Test:
        Test to_dict() method works correctly
        """
        amenity_obj = Amenity()
        amenity_obj.name = "Luxury"
        state_dict = amenity_obj.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict["name"], "Luxury")
        self.assertEqual(state_dict["__class__"], "Amenity")
        self.assertEqual(state_dict["id"], amenity_obj.id)
        self.assertEqual(
            state_dict["created_at"], amenity_obj.created_at.isoformat())
        self.assertEqual(
            state_dict["updated_at"], amenity_obj.updated_at.isoformat())

    def test_created_at_and_updated_at_are_datetime_objects(self):
        """
        Is Datetime Objects Test:
        Test created_at & updated_at are datetime objects
        """
        amenity_obj = Amenity()
        self.assertIsInstance(amenity_obj.created_at, datetime)
        self.assertIsInstance(amenity_obj.updated_at, datetime)

    def test_different_amenity_instances_have_different_ids(self):
        """
        Instance Id Test:
        Test different Amenity instance have different id's
        """
        state1 = Amenity()
        state2 = Amenity()
        self.assertNotEqual(state1.id, state2.id)

    def test_class_inheritance(self):
        """
        Class Test:
        Test if Amenity() or its instance inherits from BaseModel
        """
        amenity_obj = Amenity()
        self.assertIsInstance(amenity_obj, BaseModel)
        self.assertIsInstance(Amenity(), BaseModel)

    def test_method_inherited(self):
        """
        Method Test:
        Test inherited methods
        """
        amenity_obj = Amenity()
        self.assertTrue(hasattr(amenity_obj, "save"))
        self.assertTrue(hasattr(amenity_obj, "to_dict"))

    def test_documentations(self):
        """
        Documentation Test:
        Test if there is a doc in module, class and methods.
        """
        from models import amenity

        self.assertIsNotNone(amenity.__doc__)
        self.assertGreater(len(amenity.__doc__), 5)

        self.assertIsNotNone(Amenity.__doc__)
        self.assertGreater(len(Amenity.__doc__), 5)


if __name__ == "__main__":
    unittest.main()
