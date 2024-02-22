#!/usr/bin/python3


import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    
    def test_stateid_name(self):
        c = City()
        c.state_id = "123"
        c.name = "city"
        self.assertEqual(c.state_id, str)
        self.assertEqual(c.name, str)

    def test_id(self):
        c1 = City()
        c2 = City()
        self.assertIsInstance(c1, BaseModel)
        self.assertTrue(hasattr(c1, "id"))
        self.assertNotEqual(c1.id, c2.id)
        self.assertIsInstance(c1.id, str)
