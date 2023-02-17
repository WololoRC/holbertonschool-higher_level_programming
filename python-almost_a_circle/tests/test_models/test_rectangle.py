#!/usr/bin/python3
"""Tesr on Rectangle Class"""
import unittest
from models.rectangle import Rectangle


class Test_classRectangle(unittest.TestCase):
    def test_Rectangle_attributes(self):
        """Attrbiutes fine?"""

        """width, height, x and y"""
        instance2 = Rectangle(1, 2, 3, 4)
        self.assertEqual(instance2.width, 1)
        self.assertEqual(instance2.height, 2)
        self.assertEqual(instance2.x, 3)
        self.assertEqual(instance2.y, 4)
