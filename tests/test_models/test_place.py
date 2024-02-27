#!/usr/bin/python3


import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):

    def test_placeuserid_text(self):
        p = Place()
        p.city_id = "Somewhere"
        p.user_id = "123"
        p.name = "Place"
        p.description = "Description"
        p.number_rooms = 1
        p.number_bathrooms = 2
        p.max_guest = 3
        p.price_by_night = 4
        p.latitude = 5.6
        p.longitude = -7.8
        p.amenity_ids = ["9", "10", "11"]
        self.assertIsInstance(p.city_id, str)
        self.assertIsInstance(p.user_id, str)
        self.assertIsInstance(p.name, str)
        self.assertIsInstance(p.description, str)
        self.assertIsInstance(p.number_rooms, int)
        self.assertIsInstance(p.number_bathrooms, int)
        self.assertIsInstance(p.max_guest, int)
        self.assertIsInstance(p.price_by_night, int)
        self.assertIsInstance(p.latitude, float)
        self.assertIsInstance(p.longitude, float)
        self.assertIsInstance(p.amenity_ids, list)
        self.assertIsInstance(p.amenity_ids[0], str)

    def test_id(self):
        p1 = Place()
        p2 = Place()
        self.assertIsInstance(p1, BaseModel)
        self.assertTrue(hasattr(p1, "id"))
        self.assertNotEqual(p1.id, p2.id)
        self.assertIsInstance(p1.id, str)
