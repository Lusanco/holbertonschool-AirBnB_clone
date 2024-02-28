#!/usr/bin/python3


import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):

    def test_placeuserid_text(self):
        r = Review()
        r.place_id = "Somewhere"
        r.user_id = "Review"
        r.text = "Reviewing"
        self.assertEqual(r.place_id, str)
        self.assertEqual(r.user_id, str)
        self.assertEqual(r.text, str)
        self.assertIsInstance(r.place_id, str)
        self.assertIsInstance(r.user_id, str)
        self.assertIsInstance(r.text, str)

    def test_id(self):
        r1 = Review()
        r2 = Review()
        self.assertIsInstance(r1, BaseModel)
        self.assertTrue(hasattr(r1, "id"))
        self.assertNotEqual(r1.id, r2.id)
        self.assertIsInstance(r1.id, str)
