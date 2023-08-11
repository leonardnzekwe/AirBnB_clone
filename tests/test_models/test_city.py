#!/usr/bin/python3
"""
City class Test Module:
a class that inherits from BaseModel
"""


import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.city import City
from datetime import datetime


class TestCity(unittest.TestCase):
    """
    TestCity() class:
    a class that tests the City() class
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
        Test that City(BaseModel) instance is created properly
        """
        city_obj = City()
        self.assertIsInstance(city_obj, City)
        self.assertIsInstance(city_obj, BaseModel)
        self.assertTrue(hasattr(city_obj, "id"))
        self.assertTrue(hasattr(city_obj, "created_at"))
        self.assertTrue(hasattr(city_obj, "updated_at"))
        self.assertEqual(city_obj.state_id, "")
        self.assertEqual(city_obj.name, "")

    def test_attributes_assignment(self):
        """
        Test Attr Assignment:
        Test that class attributes are assigned correctly
        """
        city_obj = City(state_id="042", name="Top Land")
        self.assertEqual(city_obj.name, "Top Land")
        self.assertEqual(city_obj.state_id, "042")

    def test_attributes_exist_with_value(self):
        """
        Test Attr Existence:
        Test that attributes exist in User instance
        """
        city_obj = City()
        self.assertTrue(hasattr(city_obj, "state_id"))
        self.assertTrue(hasattr(city_obj, "name"))

    def test_str_representation(self):
        """
        __str__() Test:
        Test __str__() representation is correct
        """
        city_obj = City()
        city_obj.state_id = "042"
        city_obj.name = "Top Land"
        city_obj_str = str(city_obj)
        self.assertIn("[City]", city_obj_str)
        self.assertIn("'id':", city_obj_str)
        self.assertIn("'state_id': '042'", city_obj_str)
        self.assertIn("'name': 'Top Land'", city_obj_str)

    def test_save_method(self):
        """
        save() Test:
        Test save() method works correctly
        """
        city_obj = City()
        prev_updated_at = city_obj.updated_at
        city_obj.save()
        self.assertNotEqual(city_obj.updated_at, prev_updated_at)

    def test_to_dict_method(self):
        """
        to_dict() Test:
        Test to_dict() method works correctly
        """
        city_obj = City()
        city_obj.state_id = "042"
        city_obj.name = ""
        user_dict = city_obj.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict["state_id"], "042")
        self.assertEqual(user_dict["name"], "")
        self.assertEqual(user_dict["__class__"], "City")
        self.assertEqual(user_dict["id"], city_obj.id)
        self.assertEqual(
            user_dict["created_at"], city_obj.created_at.isoformat())
        self.assertEqual(
            user_dict["updated_at"], city_obj.updated_at.isoformat())

    def test_created_at_and_updated_at_are_datetime_objects(self):
        """
        Is Datetime Objects Test:
        Test created_at & updated_at are datetime objects
        """
        city_obj = City()
        self.assertIsInstance(city_obj.created_at, datetime)
        self.assertIsInstance(city_obj.updated_at, datetime)

    def test_different_city_instances_have_different_ids(self):
        """
        Instance Id Test:
        Test different City instance have different id's
        """
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)

    def test_class_inheritance(self):
        """
        Class Test:
        Test if City() or its instance inherits from BaseModel
        """
        city_obj = City()
        self.assertIsInstance(city_obj, BaseModel)
        self.assertIsInstance(City(), BaseModel)

    def test_method_inherited(self):
        """
        Method Test:
        Test inherited methods
        """
        city_obj = City()
        self.assertTrue(hasattr(city_obj, "save"))
        self.assertTrue(hasattr(city_obj, "to_dict"))

    def test_documentations(self):
        """
        Documentation Test:
        Test if there is a doc in module, class and methods.
        """
        from models import city

        self.assertIsNotNone(city.__doc__)
        self.assertGreater(len(city.__doc__), 5)

        self.assertIsNotNone(City.__doc__)
        self.assertGreater(len(City.__doc__), 5)


if __name__ == "__main__":
    unittest.main()
