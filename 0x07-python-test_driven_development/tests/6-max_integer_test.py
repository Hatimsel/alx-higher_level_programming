#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 22, -663, 44]), 44)

    def test_large_list(self):
        self.assertEqual(max_integer([9, 6, 8, 22, 88, 66, 99, 44, 775]), 775)
    def test_floats(self):
        self.assertEqual(max_integer([22.5, 56.66, 87.3, 2, 100, 255.8]), 255.8)

    def test_exceptions(self):
        with self.assertRaises(TypeError):
            max_integer(1, 2, 3)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_None(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_string(self):
        self.assertIs(max_integer('Hatim Selmun'), 'u')

    def test_one_arg(self):
        self.assertIs(max_integer([255]), 255)

if __name__ == '__main__':
    unittest.main()
