#!/usr/bin/python3
"""base test"""

import unittest
from models.base import Base


class Test_classBase(unittest.TestCase):
    """test my base class"""
    def test_is_instance(self):
        """Class exist?"""
        instance1 = Base()
        self.assertTrue(isinstance(instance1, Base))

    def test_id(self):
        """id without declarations"""
        instance1 = Base()
        self.assertEqual(instance1.id, 2)

    def test_passing_id(self):
        """id with declaration"""
        instance1 = Base(5)
        self.assertEqual(instance1.id, 5)

    def test_new_instance(self):
        """new instance how many id's?"""
        instance2 = Base()
        self.assertEqual(instance2.id, 4)

    def test_base_to_json_str(self):
        x = Base()

        """None == []"""
        return_test = x.to_json_string(None)
        self.assertEqual(return_test, "[]")

        """empty dic == []"""
        return_test = x.to_json_string({})
        self.assertEqual(return_test, "[]")

        """empty list"""
        return_test = x.to_json_string([])
        self.assertEqual(return_test, "[]")

        """it works!"""
        a_dict = {'id': 12}
        return_test = x.to_json_string([a_dict])
        self.assertTrue(isinstance(return_test, str))

        """id == 12"""
        a_dict = {'id': 12}
        return_test = x.to_json_string([a_dict])
        self.assertTrue(return_test == '[{"id": 12}]')

if __name__ == "__main__":
    unittest.main()
