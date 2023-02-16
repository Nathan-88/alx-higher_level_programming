#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
	def test_module_docstring(self):
        """Tests for module docsting"""
        m = __import__('6-max_integer').__doc__
        self.assertTrue(len(m) > 1)

    def test_function_docstring(self):
        """Tests for funstion docstring"""
        f = max_integer.__doc__
        self.assertTrue(len(f) > 1)

    def test_empty_list(self):
        """Tests for empty list []"""
        e = []
        self.assertIsNone(max_integer(e))

    def test_max_integer(self):
        result = max_integer([2,3,4,1])
        self.assertEqual(result, 4)
        self.assertEqual(max_integer([7,88,34,56]), 88)
        self.assertNotEqual(result, 2)
