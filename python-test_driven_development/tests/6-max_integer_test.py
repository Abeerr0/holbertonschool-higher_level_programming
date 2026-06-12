#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest class for max_integer"""

    def test_module_docstring(self):
        self.assertTrue(len(__import__('6-max_integer').__doc__) > 1)

    def test_function_docstring(self):
        self.assertTrue(len(max_integer.__doc__) > 1)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_no_args(self):
        self.assertEqual(max_integer(), None)

    def test_one_element(self):
        self.assertEqual(max_integer([1]), 1)

    def test_positive_end(self):
        self.assertEqual(max_integer([2, 10, 8, 36, 14, 50]), 50)

    def test_positive_middle(self):
        self.assertEqual(max_integer([2, 10, 8, 360, 14, 50]), 360)

    def test_positive_beginning(self):
        self.assertEqual(max_integer([200, 10, 8, 36, 14, 50]), 200)

    def test_one_negative(self):
        self.assertEqual(max_integer([200, 10, 8, -36, 14, 50]), 200)

    def test_all_negative(self):
        self.assertEqual(max_integer([-2, -10, -8, -36, -14, -50]), -2)

    def test_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_int_arg(self):
        with self.assertRaises(TypeError):
            max_integer([1, "string", 3])

if __name__ == "__main__":
    unittest.main()
