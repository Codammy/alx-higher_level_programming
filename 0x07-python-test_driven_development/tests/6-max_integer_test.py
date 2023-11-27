#!/usr/bin/python3
""" Python unittest for function max_integer"""


import unittest
max_integer = __import__("6-max_integer").max_integer

class TestMax(unittest.TestCase):
    """unittest for max integer"""

    def test_equals(self):
        """tests if result equals test"""
        self.assertEqual(max_integer(range(501)), 500)
        self.assertEqual(max_integer("AB"), 'B')
        self.assertEqual(max_integer([0, -1, -2, -3, -4]), 0)
        self.assertEqual(max_integer([0.1, 0.001, 0.0001, 0.010, 0.1001]), 0.1001)
        self.assertEqual(max_integer([0.1, 0.001, 1, 0.010, 0.1001]), 1)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([]), None)
    
    def test_type(self):
        """type check args"""
        self.assertRaises(TypeError, max_integer, 1)
        self.assertRaises(TypeError, max_integer, None)
