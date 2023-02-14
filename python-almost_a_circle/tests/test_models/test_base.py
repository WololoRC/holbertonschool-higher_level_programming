#!/usr/bin/python3
"""base test"""

import unittest
from models.base import Base


class testBase(unittest.TestCase):
    """test my base class"""
    def test_is_instance(self):
        """Class exist?"""
        instance1 = Base()
        self.assertTrue(isinstance(instance1, Base))

    def test_id(self):
        """id without declarations"""
        instance1 = Base()
        self.assertEqual(instance1.id, 1)

    def test_passing_id(self):
        """id with declaration"""
        instance1 = Base(5)
        self.assertEqual(instance1.id, 5)

    def test_new_instance(self):
        """new instance + 1 id?"""
        instance2 = Base()
        self.assertEqual(instance2.id, 3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
