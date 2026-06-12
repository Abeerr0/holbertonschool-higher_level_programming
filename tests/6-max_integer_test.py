#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function."""

    def test_regular_lists(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)

    def test_single_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-5, 10, 0, -2]), 10)
