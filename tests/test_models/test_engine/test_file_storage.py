#!/usr/binpython3
"""
FileStorage Test Module
"""


from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
import unittest


class TestFileStorage(unittest.TestCase):
    """
    FileStorage Test class
    """

    def setUp(self):
        """
        setUp() instance method:
        Create a new instance of FileStorage before each test
        """
        self.file_storage = FileStorage()

    def tearDown(self):
        """
        tearDown() instance method:
        Clean up by removing the test JSON file if it exists after each test
        """
        if os.path.exists(self.file_storage._FileStorage__file_path):
            os.remove(self.file_storage._FileStorage__file_path)

    def test_all(self):
        """
        Test all() method:
        The test ensures that the all() method returns a dictionary
        containing the stored objects.
        """
        objects = self.file_storage.all()
        self.assertIsInstance(objects, dict)

    def test_new(self):
        """
        Test new() method:
        The test verifies that the new() method correctly adds a new object
        to the __objects dictionary using the appropriate key.
        """
        base_model = BaseModel()
        self.file_storage.new(base_model)
        key = f"{base_model.__class__.__name__}.{base_model.id}"
        self.assertIn(key, self.file_storage.all())

    def test_save_and_reload(self):
        """
        Test save() and reload() methods:
        The test confirms that the save() method properly serializes
        the objects to a JSON file and that the
        reload() successfully deserializes
        the JSON file back into the __objects dictionary.
        """
        base_model = BaseModel()
        self.file_storage.new(base_model)
        self.file_storage.save()
        new_file_storage = FileStorage()
        new_file_storage.reload()
        key = f"{base_model.__class__.__name__}.{base_model.id}"
        self.assertIn(key, new_file_storage.all())

    def test_new_overwrite_existing(self):
        """
        Test new() method overwriting existing object:
        Verify that new() overwrites an existing object in __objects.
        """
        base_model1 = BaseModel()
        self.file_storage.new(base_model1)
        key = f"{base_model1.__class__.__name__}.{base_model1.id}"

        base_model2 = BaseModel()
        self.file_storage.new(base_model2)
        self.assertIn(key, self.file_storage.all())

    def test_new_overwrite_existing(self):
        """
        Test new() method overwriting existing object:
        Verify that new() overwrites an existing object in __objects.
        """
        base_model1 = BaseModel()
        self.file_storage.new(base_model1)
        key = f"{base_model1.__class__.__name__}.{base_model1.id}"

        base_model2 = BaseModel()
        self.file_storage.new(base_model2)
        self.assertIn(key, self.file_storage.all())


if __name__ == "__main__":
    unittest.main()
