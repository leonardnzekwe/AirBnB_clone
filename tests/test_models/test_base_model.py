#!/usr/bin/python3
"""
BaseModel Test Module
"""


from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from uuid import UUID
import os
import unittest


class TestBaseModel(unittest.TestCase):
    """
    BaseModel Test class
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

    def test_init_defaults(self):
        """
        Initialization Test:
        Test if the BaseModel object is initialized correctly
        Test if the BaseModel instance can be created without any arguments.
        """
        base_model = BaseModel()
        self.assertIsInstance(base_model, BaseModel)
        self.assertIsNotNone(base_model)

    def test_init_with_args(self):
        """
        With *args Test:
        Test for creation with an argument
        and the value won't be in __dict__
        """
        additional_arg = "additional_argument"
        base_model = BaseModel(additional_arg)
        self.assertIsNotNone(base_model)
        self.assertNotIn(additional_arg, base_model.__dict__)

    def test__init_with_args_and_kwargs(self):
        """
        With *args, *kwargs Test:
        Test for creation with an argument
        and the value or key/value won't be in __dict__
        """
        additional_arg = "additional_argument"
        additional_kwarg = "additional_kwarg_value"
        base_model = BaseModel(additional_arg, key=additional_kwarg)
        self.assertIsNotNone(base_model)
        self.assertNotIn(additional_arg, base_model.__dict__)
        self.assertIn("key", base_model.__dict__)

    def test_init_with_valid_kwargs(self):
        """
        With valid *kwargs Test:
        Test for creation with an argument
        and the key/value is set correctly and in __dict__
        """
        valid_kwargs = {
            "id": "valid_id",
            "created_at": "2023-08-08T12:34:56.789",
            "updated_at": "2023-08-08T12:34:56.789",
            "custom_attribute": "custom_value",
        }
        base_model = BaseModel(**valid_kwargs)
        self.assertIsNotNone(base_model)
        self.assertEqual(base_model.id, "valid_id")
        self.assertEqual(base_model.created_at.year, 2023)
        self.assertEqual(base_model.custom_attribute, "custom_value")
        self.assertIn("id", base_model.__dict__)

    def test_init_invalid_created_at_format(self):
        """
        With invalid *kwargs Test:
        Test if an error is raised when created_at
        has an invalid datetime format.
        """
        invalid_kwargs = {"created_at": "invalid_datetime_format"}
        with self.assertRaises(ValueError):
            BaseModel(**invalid_kwargs)

    def test_init_class_keyword(self):
        """
        With class Keyword (__class__) Test:
        Test if __class__ keyword is ignored
        when initializing attributes.
        """
        class_keyword_kwargs = {
            "__class__": "ClassKeyWord",
            "custom_attribute": "custom_value",
        }
        base_model = BaseModel(**class_keyword_kwargs)
        self.assertIsNotNone(base_model)
        self.assertEqual(base_model.custom_attribute, "custom_value")
        self.assertNotIn("__class__", base_model.__dict__)

    def test_init_empty_kwargs(self):
        """
        With Empty Keyword Arguments (**kwargs) Test:
        Test if the BaseModel instance can be created
        with empty keyword arguments using **kwargs.
        Instance should be created with default values.
        """
        base_model = BaseModel(**{})
        self.assertIsNotNone(base_model)

    def test_id_generation(self):
        """
        ID Generation Test:
        Test if the id attribute is generated properly.
        """
        base_model1 = BaseModel()
        base_model2 = BaseModel()
        self.assertIsNotNone(base_model1.id)
        self.assertIsNotNone(base_model2.id)
        self.assertIsInstance(base_model1.id, str)
        self.assertIsInstance(base_model2.id, str)
        self.assertNotEqual(base_model1.id, base_model2.id)
        self.assertIsInstance(UUID(base_model1.id), UUID)
        self.assertIsInstance(UUID(base_model2.id), UUID)

    def test_specific_id(self):
        """
        Specific ID Test:
        Test if the BaseModel instance can be created with a specific ID.
        """
        specific_id = "test-id-123"
        base_model = BaseModel()
        base_model.id = specific_id
        self.assertEqual(base_model.id, specific_id)

    def test_created_updated_time(self):
        """
        Creation and Update Time Test:
        Test if the created_at and updated_at attributes are set correctly.
        """
        base_model = BaseModel()
        base_model2 = BaseModel()
        self.assertIsNotNone(base_model.created_at)
        self.assertIsNotNone(base_model.updated_at)
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)
        self.assertEqual(base_model.created_at, base_model.updated_at)
        self.assertTrue(base_model.created_at < base_model2.created_at)

    def test_str_representation(self):
        """
        String Representation Test:
        Test if the __str__() returns the expected string representation.
        """
        base_model = BaseModel()
        expected_str = f"[BaseModel] ({base_model.id}) {base_model.__dict__}"
        self.assertEqual(str(base_model), expected_str)

    def test_save_method(self):
        """
        Save Method Test:
        Test if the save method updates the updated_at attribute.
        """
        base_model = BaseModel()
        prev_updated_at = base_model.updated_at
        base_model.save()
        self.assertNotEqual(base_model.updated_at, prev_updated_at)

    def test_to_dict_method(self):
        """
        to_dict Method Test:
        Test if the to_dict() method returns a dictionary
        with the correct attributes.
        """
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertIsInstance(base_model_dict, dict)
        self.assertIn("__class__", base_model_dict)
        self.assertEqual(base_model_dict["__class__"], "BaseModel")
        self.assertIn("created_at", base_model_dict)
        self.assertIn("updated_at", base_model_dict)

    def test_to_dict_attributes(self):
        """
        Attributes Preservation in to_dict Test:
        Test if the to_dict() preserves all attributes in the dictionary.
        """
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        for key, value in base_model.__dict__.items():
            self.assertIn(key, base_model_dict)
            if isinstance(value, datetime):
                self.assertEqual(base_model_dict[key], value.isoformat())
            else:
                self.assertEqual(base_model_dict[key], value)

    def test_to_dict_date_format(self):
        """
        Date Format in to_dict Test:
        Test if the dates in the to_dict output are in the correct ISO format.
        """
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertTrue(datetime.fromisoformat(base_model_dict["created_at"]))
        self.assertTrue(datetime.fromisoformat(base_model_dict["updated_at"]))

    def test_equality(self):
        """
        Equality Test:
        Test if two instances of BaseModel with the same attributes
        are considered equal.
        """
        base_model1 = BaseModel()
        base_model2 = BaseModel()
        self.assertNotEqual(base_model1, base_model2)

    def test_storage_attr(self):
        """
        Test Filestorage storage atrribute:
        Test if there is obj_id in storage class atrr__objects
        which is a dict
        """
        base_model = BaseModel()
        self.assertIn(
            f"{base_model.__class__.__name__}.{base_model.id}", storage.all()
        )

    def test_documentations(self):
        """
        Documentation Test:
        Test if there is a doc in module, class and methods.
        """
        from models import base_model

        self.assertIsNotNone(base_model.__doc__)
        self.assertGreater(len(base_model.__doc__), 5)

        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertGreater(len(BaseModel.__init__.__doc__), 5)

        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertGreater(len(BaseModel.__str__.__doc__), 5)

        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertGreater(len(BaseModel.save.__doc__), 5)

        self.assertIsNotNone(BaseModel.to_dict.__doc__)
        self.assertGreater(len(BaseModel.to_dict.__doc__), 5)


if __name__ == "__main__":
    unittest.main()
