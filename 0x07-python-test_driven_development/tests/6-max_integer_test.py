#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_find_max(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([50, 20, 49, 55, -70000]), 55)

    def test_empty(self):
        self.assertIsNone(max_integer([]))

    def test_negatives(self):
        self.assertEqual(max_integer([-20, -60, -1, -999]), -1)

#     def test_string_in(self):
#         with self.assertRaises(TypeError, "NoneType object does not support the context manager protocol"):
#             max_int([12, 5, 'str', 5])
    def test_large_list(self):
        self.assertEqual(max_integer([15, 1500000, 69, 35, -355555555, 66599, 55558, 4447, 0, 66210, 88549, 15572, 3333333390, 159700000000, -2000000]), 159700000000)

    def test_one_element_list(self):
        self.assertEqual(max_integer([38]), 38)

    def test_duplicate_max(self):
        self.assertEqual(max_integer([55, 96, 4, 0, 96, 32]), 96)

    def test_leading_zeros(self):
        self.assertEqual(max_integer([0o1547, 0o77, 0o5, 0o54, 0o645]), 0o1547)
