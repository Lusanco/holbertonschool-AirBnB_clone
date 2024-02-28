#!/usr/bin/python3

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):

    def test_name(self):
        a = Amenity()
        a.name = "Amenity"
        self.assertEqual(a.name, str)
        self.assertIsInstance(a.name, str)

    def test_id(self):
        a1 = Amenity()
        a2 = Amenity()
        self.assertIsInstance(a1, BaseModel)
        self.assertTrue(hasattr(a1, "id"))
        self.assertNotEqual(a1.id, a2.id)
        self.assertIsInstance(a1.id, str)
