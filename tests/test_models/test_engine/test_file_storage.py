#!/usr/binpython3
"""
FileStorage Test Module
"""


from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
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

    def test_attr(self):
        """
        Test FileStorage class attributes
        """
        store = FileStorage()
        self.assertTrue(store, "classes")
        self.assertTrue(store, "_FileStorage__file_path")
        self.assertTrue(store, "_FileStorage__objects")

    def test_classes_attribute(self):
        """
        Test FileStorage classes attribute dict values
        """
        expected_classes = {
            "BaseModel": BaseModel, "User": User, "State": State,
            "City": City, "Amenity": Amenity, "Place": Place,
            "Review": Review
        }
        self.assertDictEqual(FileStorage.classes_dict, expected_classes)

    def test_documentations(self):
        """
        Documentation Test:
        Test if there is a doc in module, class and methods.
        """
        from models.engine import file_storage

        self.assertIsNotNone(file_storage.__doc__)
        self.assertGreater(len(file_storage.__doc__), 5)

        self.assertIsNotNone(FileStorage.__doc__)
        self.assertGreater(len(FileStorage.__doc__), 5)

        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertGreater(len(FileStorage.all.__doc__), 5)

        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertGreater(len(FileStorage.new.__doc__), 5)

        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertGreater(len(FileStorage.save.__doc__), 5)

        self.assertIsNotNone(FileStorage.reload.__doc__)
        self.assertGreater(len(FileStorage.reload.__doc__), 5)


if __name__ == "__main__":
    unittest.main()
