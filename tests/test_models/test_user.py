#!/usr/bin/python3


import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):

    def test_email_pass_names(self):
        u = User()
        u.email = "user@email.com"
        u.password = "secretpass"
        u.first_name = "User"
        u.last_name = "Somebaddie"
        self.assertEqual(u.email, str)
        self.assertEqual(u.password, str)
        self.assertEqual(u.first_name, str)
        self.assertEqual(u.last_name, str)

    def test_id(self):
        u1 = User()
        u2 = User()
        self.assertIsInstance(u1, BaseModel)
        self.assertTrue(hasattr(u1, "id"))
        self.assertNotEqual(u1.id, u2.id)
        self.assertIsInstance(u1.id, str)
