#!/usr/bin/python3

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_id(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertIsInstance(b1, BaseModel)
        self.assertTrue(hasattr(b1, "id"))
        self.assertNotEqual(b1.id, b2.id)
        self.assertIsInstance(b1.id, str)

    def test_str(self):
        b1 = BaseModel()
        self.assertIsInstance(b1.__str__, str)
