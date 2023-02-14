#!/usr/bin/python3
"""base test"""

import unittest
from models.base import Base

class testBase(unittest.TestCase):
    def test_is_instance(self):
        instance1 = Base()
        self.assertTrue(isinstance(instance1, Base))
    def test_id(self):
        instance1 = Base()
        self.assertEqual(instance1.id, 1)

if __name__ == "__main__":
    unittest.main(verbosity=2)
