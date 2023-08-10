#!/usr/bin/python3
"""
Place class Test Module:
a class that inherits from BaseModel
"""


import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.place import Place
from datetime import datetime


class TestPlace(unittest.TestCase):
    """
    TestPlace() class:
    a class that tests the Place() class
    """
    @classmethod
    def setUp(cls):
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
        Test that Place(BaseModel) instance is created properly
        """
        place_obj = Place()
        self.assertIsInstance(place_obj, Place)
        self.assertIsInstance(place_obj, BaseModel)
        self.assertTrue(hasattr(place_obj, "id"))
        self.assertTrue(hasattr(place_obj, "created_at"))
        self.assertTrue(hasattr(place_obj, "updated_at"))
        self.assertEqual(place_obj.city_id, "")
        self.assertEqual(place_obj.user_id, "")
        self.assertEqual(place_obj.name, "")
        self.assertEqual(place_obj.description, "")
        self.assertEqual(place_obj.number_rooms, 0)
        self.assertEqual(place_obj.number_bathrooms, 0)
        self.assertEqual(place_obj.max_guest, 0)
        self.assertEqual(place_obj.price_by_night, 0)
        self.assertEqual(place_obj.latitude, 0.0)
        self.assertEqual(place_obj.longitude, 0.0)
        self.assertEqual(place_obj.amenity_ids, [])

    def test_attributes_assignment(self):
        """
        Test Attr Assignment:
        Test that class attributes are assigned correctly
        """
        place_obj = Place(
            city_id="city_id", user_id="user_id",
            name="name", description="description",
            number_rooms=5, number_bathrooms=3, max_guest=8,
            price_by_night=200, latitude=40.7128, longitude=-74.0060,
            amenity_ids=["amenity_id1", "amenity_id2"]
        )
        self.assertEqual(place_obj.city_id, "city_id")
        self.assertEqual(place_obj.user_id, "user_id")
        self.assertEqual(place_obj.name, "name")
        self.assertEqual(place_obj.description, "description")
        self.assertEqual(place_obj.number_rooms, 5)
        self.assertEqual(place_obj.number_bathrooms, 3)
        self.assertEqual(place_obj.max_guest, 8)
        self.assertEqual(place_obj.price_by_night, 200)
        self.assertEqual(place_obj.latitude, 40.7128)
        self.assertEqual(place_obj.longitude, -74.0060)
        self.assertEqual(place_obj.amenity_ids, ["amenity_id1", "amenity_id2"])

    def test_attributes_exist_with_value(self):
        """
        Test Attr Existence:
        Test that attributes exist in User instance
        """
        place_obj = Place()
        self.assertTrue(hasattr(place_obj, "city_id"))
        self.assertTrue(hasattr(place_obj, "user_id"))
        self.assertTrue(hasattr(place_obj, "name"))
        self.assertTrue(hasattr(place_obj, "description"))
        self.assertTrue(hasattr(place_obj, "number_rooms"))
        self.assertTrue(hasattr(place_obj, "number_bathrooms"))
        self.assertTrue(hasattr(place_obj, "max_guest"))
        self.assertTrue(hasattr(place_obj, "price_by_night"))
        self.assertTrue(hasattr(place_obj, "latitude"))
        self.assertTrue(hasattr(place_obj, "longitude"))
        self.assertTrue(hasattr(place_obj, "max_guest"))
        self.assertTrue(hasattr(place_obj, "amenity_ids"))

    def test_str_representation(self):
        """
        __str__() Test:
        Test __str__() representation is correct
        """
        place_obj = Place()
        place_obj.city_id = "city_id"
        place_obj.user_id = "user_id"
        place_obj_str = str(place_obj)
        self.assertIn("[Place]", place_obj_str)
        self.assertIn("'id':", place_obj_str)
        self.assertIn("'city_id': 'city_id'", place_obj_str)
        self.assertIn("'user_id': 'user_id'", place_obj_str)

    def test_save_method(self):
        """
        save() Test:
        Test save() method works correctly
        """
        place_obj = Place()
        prev_updated_at = place_obj.updated_at
        place_obj.save()
        self.assertNotEqual(place_obj.updated_at, prev_updated_at)

    def test_to_dict_method(self):
        """
        to_dict() Test:
        Test to_dict() method works correctly
        """
        place_obj = Place()
        place_obj.city_id = "city_id"
        place_obj.name = ""
        place_obj.description = ""
        place_obj.user_id = ""
        place_dict = place_obj.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertEqual(place_dict["city_id"], "city_id")
        self.assertEqual(place_dict["user_id"], "")
        self.assertEqual(place_dict["name"], "")
        self.assertEqual(place_dict["description"], "")
        self.assertEqual(place_dict["__class__"], "Place")
        self.assertEqual(place_dict["id"], place_obj.id)
        self.assertEqual(
            place_dict["created_at"], place_obj.created_at.isoformat())
        self.assertEqual(
            place_dict["updated_at"], place_obj.updated_at.isoformat())

    def test_created_at_and_updated_at_are_datetime_objects(self):
        """
        Is Datetime Objects Test:
        Test created_at & updated_at are datetime objects
        """
        place_obj = Place()
        self.assertIsInstance(place_obj.created_at, datetime)
        self.assertIsInstance(place_obj.updated_at, datetime)

    def test_different_place_instances_have_different_ids(self):
        """
        Instance Id Test:
        Test different Place instance have different id's
        """
        place1 = Place()
        place2 = Place()
        self.assertNotEqual(place1.id, place2.id)

    def test_class_inheritance(self):
        """
        Class Test:
        Test if Place() or its instance inherits from BaseModel
        """
        place_obj = Place()
        self.assertIsInstance(place_obj, BaseModel)
        self.assertIsInstance(Place(), BaseModel)

    def test_method_inherited(self):
        """
        Method Test:
        Test inherited methods
        """
        place_obj = Place()
        self.assertTrue(hasattr(place_obj, "save"))
        self.assertTrue(hasattr(place_obj, "to_dict"))

    def test_documentations(self):
        """
        Documentation Test:
        Test if there is a doc in module, class and methods.
        """
        from models import place

        self.assertIsNotNone(place.__doc__)
        self.assertGreater(len(place.__doc__), 5)

        self.assertIsNotNone(Place.__doc__)
        self.assertGreater(len(Place.__doc__), 5)


if __name__ == "__main__":
    unittest.main()
