#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer."""
    
    def test_regular(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        
    def test_empty(self):
        self.assertEqual(max_integer([]), None)
        
    def test_negative(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        
    def test_one_element(self):
        self.assertEqual(max_integer([5]), 5)
        
    def test_floats(self):
        self.assertEqual(max_integer([1.5, 6.3, -9.1, 15.2]), 15.2)

if __name__ == '__main__':
    unittest.main()
