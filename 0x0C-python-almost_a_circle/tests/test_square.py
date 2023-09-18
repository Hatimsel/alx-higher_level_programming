#!/usr/bin/python3
"""
Testing Square class and its methods
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    TestSquare class for testing Square class
    """
    def setUp(self):
        """
        Initiallinzing the private class attribute nb_objects in each test
        """
        Base._Base__nb_objects = 0

    def test_inheritance(self):
        """
        Testing the class's inheritance
        """
        s = Square(5)
        self.assertIsInstance(s, Square)
        self.assertIsInstance(s, Rectangle)

    def test_basic(self):
        """
        Testing basic tests
        """
        s1 = Square(5)
        self.assertEqual(s1.__str__(), '[Square] (1) 0/0 - 5')
        self.assertEqual(s1.area(), 25)

        s2 = Square(2, 2)
        self.assertEqual(s2.__str__(), '[Square] (2) 2/0 - 2')
        self.assertEqual(s2.area(), 4)

        s3 = Square(3, 1, 3)
        self.assertEqual(s3.__str__(), '[Square] (3) 1/3 - 3')
        self.assertEqual(s3.area(), 9)

    def test_square_exceptions(self):
        """
        Testing square exceptions when integer validator fails
        """
        with self.assertRaises(TypeError):
            s = Square('2', 2)

        with self.assertRaises(TypeError):
            s = Square(5, '3', 6)

        with self.assertRaises(TypeError):
            s = Square(5, 3, '1')

        with self.assertRaises(ValueError):
            s = Square(0, 3)

        with self.assertRaises(ValueError):
            s = Square(6, -3, 1)

        with self.assertRaises(ValueError):
            s = Square(6, 3, -6)

    def test_with_no_parameter(self):
        """
        Testing Square object with no arguments
        """
        with self.assertRaises(TypeError):
            s = Square()

    def test_with_more_parameters(self):
        """
        Testing Square object with more arguments
        """
        with self.assertRaises(TypeError):
            s = Square(2, 5, 3, 4, 12, 4)

    def test_size(self):
        """
        Testing the size method
        """
        s1 = Square(5)
        self.assertEqual(s1.__str__(), '[Square] (1) 0/0 - 5')
        self.assertEqual(s1.size, 5)

        s2 = Square(4)
        self.assertEqual(s2.__str__(), '[Square] (2) 0/0 - 4')
        self.assertEqual(s2.size, 4)

        s1.size = 10
        self.assertEqual(s1.__str__(), '[Square] (1) 0/0 - 10')

        with self.assertRaises(TypeError):
            s1.size = '2'

        with self.assertRaises(TypeError):
            s1.size = [1]

        with self.assertRaises(TypeError):
            s1.size = {'a': 2}

    def test_square_display(self):
        """
        Testing Square display method
        """
        from io import StringIO
        import sys

        s = Square(3)

        captured_output = StringIO()
        sys.stdout = captured_output

        s.display()
        sys.stdout = sys.__stdout__

        result = captured_output.getvalue()
        expected_result = '###\n###\n###\n'

        self.assertEqual(result, expected_result)
        self.assertEqual(s.display(), None)

        s = Square(3, 2, 2)

        captured_output = StringIO()
        sys.stdout = captured_output

        s.display()
        sys.stdout = sys.__stdout__

        result = captured_output.getvalue()
        expected_result = '\n\n  ###\n  ###\n  ###\n'

        self.assertEqual(result, expected_result)

    def test_update(self):
        """
        Testing the update() method
        """
        s1 = Square(5)
        self.assertEqual(s1.__str__(), '[Square] (1) 0/0 - 5')

        s1.update(10)
        self.assertEqual(s1.__str__(), '[Square] (10) 0/0 - 5')

        s1.update(1, 2)
        self.assertEqual(s1.__str__(), '[Square] (1) 0/0 - 2')

        s1.update(1, 2, 3)
        self.assertEqual(s1.__str__(), '[Square] (1) 3/0 - 2')

        s1.update(1, 2, 3, 4)
        self.assertEqual(s1.__str__(), '[Square] (1) 3/4 - 2')

        s1.update(x=12)
        self.assertEqual(s1.__str__(), '[Square] (1) 12/4 - 2')

        s1.update(size=7, y=1)
        self.assertEqual(s1.__str__(), '[Square] (1) 12/1 - 7')

        s1.update(size=7, id=89, y=1)
        self.assertEqual(s1.__str__(), '[Square] (89) 12/1 - 7')

    def test_square_to_dictionary(self):
        """
        Testing to_dictionary method
        """
        s1 = Square(10, 2, 1)
        self.assertEqual(s1.__str__(), '[Square] (1) 2/1 - 10')

        s1_dictionary = s1.to_dictionary()
        expected_result = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(s1_dictionary, expected_result)
        self.assertTrue(type(s1_dictionary) == dict)

        s2 = Square(1, 1)
        self.assertEqual(s2.__str__(), '[Square] (2) 1/0 - 1')

        s2.update(**s1_dictionary)
        self.assertEqual(s2.__str__(), '[Square] (1) 2/1 - 10')

        self.assertFalse(s1 == s2)

    if __name__ == "__main__":
        unittest.main()
