#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """unit testing"""
    def test_max_integer(self):
        result = max_integer([2,3,4,1])
        self.assertEqual(result, 4)
        self.assertEqual(max_integer([7,88,34,56]), 88)
        self.assertNotEqual(result, 2)
