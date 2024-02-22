#!/usr/bin/python3


import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    
    def test_name(self):
        s = State()
        s.name = "State"
        self.assertEqual(s.name, str)

    def test_id(self):
        s1 = State()
        s2 = State()
        self.assertIsInstance(s1, BaseModel)
        self.assertTrue(hasattr(s1, "id"))
        self.assertNotEqual(s1.id, s2.id)
        self.assertIsInstance(s1.id, str)
