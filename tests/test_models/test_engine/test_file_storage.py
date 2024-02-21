#!/usr/bin/python3

import json
import os
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from unittest.mock import patch

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """Set up for the tests"""
        self.storage = FileStorage()
        self.model = BaseModel()
        self.model.save()

    def test_file_path(self):
        """Test the __file_path attribute"""
        self.assertTrue(hasattr(self.storage, "_FileStorage__file_path"))
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")

    def test_objects(self):
        """Test the __objects attribute"""
        self.assertTrue(hasattr(self.storage, "_FileStorage__objects"))
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test_all(self):
        """Test the all() method"""
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertTrue(len(all_objects) > 0)

    def test_new(self):
        """Test the new() method"""
        initial_count = len(self.storage.all())
        new_model = BaseModel()
        self.storage.new(new_model)
        new_count = len(self.storage.all())
        self.assertEqual(new_count, initial_count + 1)

    def test_save(self):
        """Test the save() method"""
        self.model.name = "Test Model"
        self.model.save()
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json", "r") as f:
            data = json.load(f)
            key = f"BaseModel.{self.model.id}"
            self.assertIn(key, data)
            self.assertEqual(data[key]["name"], "Test Model")

    def test_reload(self):
        """Test the reload() method"""
        self.model.name = "Test Reload"
        self.model.save()
        self.storage.reload()
        all_objects = self.storage.all()
        key = f"BaseModel.{self.model.id}"
        self.assertIn(key, all_objects)
        self.assertEqual(all_objects[key].name, "Test Reload")

    def tearDown(self):
        """Tear down the tests"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    unittest.main()
