#!/usr/bin/python3
"""
Review class Test Module:
a class that inherits from BaseModel
"""


import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.review import Review
from datetime import datetime


class TestReview(unittest.TestCase):
    """
    TestReview() class:
    a class that tests the Review() class
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
        Test that Review(BaseModel) instance is created properly
        """
        review_obj = Review()
        self.assertIsInstance(review_obj, Review)
        self.assertIsInstance(review_obj, BaseModel)
        self.assertTrue(hasattr(review_obj, "id"))
        self.assertTrue(hasattr(review_obj, "created_at"))
        self.assertTrue(hasattr(review_obj, "updated_at"))
        self.assertEqual(review_obj.place_id, "")
        self.assertEqual(review_obj.user_id, "")
        self.assertEqual(review_obj.text, "")

    def test_attributes_assignment(self):
        """
        Test Attr Assignment:
        Test that class attributes are assigned correctly
        """
        review_obj = Review(
            place_id="place_id", user_id="user_id",
            text="text"
        )
        self.assertEqual(review_obj.place_id, "place_id")
        self.assertEqual(review_obj.user_id, "user_id")
        self.assertEqual(review_obj.text, "text")

    def test_attributes_exist_with_value(self):
        """
        Test Attr Existence:
        Test that attributes exist in User instance
        """
        review_obj = Review()
        self.assertTrue(hasattr(review_obj, "place_id"))
        self.assertTrue(hasattr(review_obj, "user_id"))
        self.assertTrue(hasattr(review_obj, "text"))

    def test_str_representation(self):
        """
        __str__() Test:
        Test __str__() representation is correct
        """
        review_obj = Review()
        review_obj.place_id = "place_id"
        review_obj.user_id = "user_id"
        review_obj_str = str(review_obj)
        self.assertIn("[Review]", review_obj_str)
        self.assertIn("'id':", review_obj_str)
        self.assertIn("'place_id': 'place_id'", review_obj_str)
        self.assertIn("'user_id': 'user_id'", review_obj_str)

    def test_save_method(self):
        """
        save() Test:
        Test save() method works correctly
        """
        review_obj = Review()
        prev_updated_at = review_obj.updated_at
        review_obj.save()
        self.assertNotEqual(review_obj.updated_at, prev_updated_at)

    def test_to_dict_method(self):
        """
        to_dict() Test:
        Test to_dict() method works correctly
        """
        review_obj = Review()
        review_obj.place_id = "place_id"
        review_obj.text = ""
        review_obj.last_name = ""
        review_obj.user_id = ""
        user_dict = review_obj.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict["place_id"], "place_id")
        self.assertEqual(user_dict["user_id"], "")
        self.assertEqual(user_dict["text"], "")
        self.assertEqual(user_dict["__class__"], "Review")
        self.assertEqual(user_dict["id"], review_obj.id)
        self.assertEqual(
            user_dict["created_at"], review_obj.created_at.isoformat())
        self.assertEqual(
            user_dict["updated_at"], review_obj.updated_at.isoformat())

    def test_created_at_and_updated_at_are_datetime_objects(self):
        """
        Is Datetime Objects Test:
        Test created_at & updated_at are datetime objects
        """
        review_obj = Review()
        self.assertIsInstance(review_obj.created_at, datetime)
        self.assertIsInstance(review_obj.updated_at, datetime)

    def test_different_review_instances_have_different_ids(self):
        """
        Instance Id Test:
        Test different Review instance have different id's
        """
        review1 = Review()
        review2 = Review()
        self.assertNotEqual(review1.id, review2.id)

    def test_class_inheritance(self):
        """
        Class Test:
        Test if Review() or its instance inherits from BaseModel
        """
        review_obj = Review()
        self.assertIsInstance(review_obj, BaseModel)
        self.assertIsInstance(Review(), BaseModel)

    def test_method_inherited(self):
        """
        Method Test:
        Test inherited methods
        """
        review_obj = Review()
        self.assertTrue(hasattr(review_obj, "save"))
        self.assertTrue(hasattr(review_obj, "to_dict"))

    def test_documentations(self):
        """
        Documentation Test:
        Test if there is a doc in module, class and methods.
        """
        from models import review

        self.assertIsNotNone(review.__doc__)
        self.assertGreater(len(review.__doc__), 5)

        self.assertIsNotNone(Review.__doc__)
        self.assertGreater(len(Review.__doc__), 5)


if __name__ == "__main__":
    unittest.main()
