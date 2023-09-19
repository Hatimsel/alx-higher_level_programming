#!/usr/bin/python3
"""
Testing Rectangle class
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """
    TestRectangle class for testing the class's methods
    """
    def setUp(self):
        """
        Initiallizing the private class attribute nb_objects to 0
        """
        Base._Base__nb_objects = 0

    def test_basic(self):
        """
        Running basic tests
        """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_is_instance(self):
        """
        Checks if Rectangle is an instance of class Base
        """
        r = Rectangle(2, 4)
        self.assertIsInstance(r, Base)

    def test_exceptions(self):
        """
        Testing exceptions when an attribute is not valid
        """
        with self.assertRaises(TypeError):
            r = Rectangle('4', 2, 5)

        with self.assertRaises(TypeError):
            r = Rectangle(4, '2', 3)

        with self.assertRaises(TypeError):
            r = Rectangle(4, 2, '3', 3)

        with self.assertRaises(TypeError):
            r = Rectangle(4, 2, 3, '3')

        with self.assertRaises(ValueError):
            r = Rectangle(0, 2)

        with self.assertRaises(ValueError):
            r = Rectangle(2, 0)

        with self.assertRaises(ValueError):
            r = Rectangle(2, 4, -2, 1)

        with self.assertRaises(ValueError):
            r = Rectangle(2, 4, 3, -1)
        # after checking the QA reviws
        with self.assertRaises(ValueError):
            r = Rectangle(-2, 4, 3, 1)

        with self.assertRaises(ValueError):
            r = Rectangle(2, -2, 3, 1)

    def test_with_no_parameter(self):
        """
        Testing Rectangle object with no arguments
        """
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_with_more_parameters(self):
        """
        Testing Rectangle object with more arguments
        """
        with self.assertRaises(TypeError):
            r = Rectangle(2, 5, 3, 3, 12, 4)

    def test_area(self):
        """
        Testing the area() method efficency
        """
        r = Rectangle(2, 4)
        self.assertEqual(r.area(), 8)

        r1 = Rectangle(7, 10)
        self.assertEqual(r1.area(), 70)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_display(self):
        """
        Testing the display() method
        """
        import sys
        from io import StringIO

        r1 = Rectangle(2, 3)

        captured_output = StringIO()
        sys.stdout = captured_output

        r1.display()
        sys.stdout = sys.__stdout__

        result = captured_output.getvalue()
        expected_result = '##\n##\n##\n'

        self.assertEqual(result, expected_result)
        self.assertEqual(r1.display(), None)

        r2 = Rectangle(2, 2, 2, 2)

        captured_output = StringIO()
        sys.stdout = captured_output

        r2.display()
        sys.stdout = sys.__stdout__

        result = captured_output.getvalue()
        expected_result = '\n\n  ##\n  ##\n'

        self.assertEqual(result, expected_result)

    def test_str(self):
        """
        Testing dunder __str__
        """
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), '[Rectangle] (12) 2/1 - 4/6')

        r2 = Rectangle(5, 5, 1)
        self.assertEqual(r2.__str__(), '[Rectangle] (1) 1/0 - 5/5')

    def test_update_args(self):
        """
        Testing the update method
        """
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(r1.__str__(), '[Rectangle] (1) 10/10 - 10/10')

        r1.update(89)
        self.assertEqual(r1.__str__(), '[Rectangle] (89) 10/10 - 10/10')

        r1.update(89, 2)
        self.assertEqual(r1.__str__(), '[Rectangle] (89) 10/10 - 2/10')

        r1.update(89, 2, 3)
        self.assertEqual(r1.__str__(), '[Rectangle] (89) 10/10 - 2/3')

        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.__str__(), '[Rectangle] (89) 4/10 - 2/3')

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), '[Rectangle] (89) 4/5 - 2/3')

    def test_update_kwargs(self):
        """
        Testing the update method with kwargs
        """
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(r1.__str__(), '[Rectangle] (1) 10/10 - 10/10')

        r1.update(height=1)
        self.assertEqual(r1.__str__(), '[Rectangle] (1) 10/10 - 10/1')

        r1.update(width=1, x=2)
        self.assertEqual(r1.__str__(), '[Rectangle] (1) 2/10 - 1/1')

        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r1.__str__(), '[Rectangle] (89) 3/1 - 2/1')

        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r1.__str__(), '[Rectangle] (89) 1/3 - 4/2')

    def test_to_dictionary(self):
        """
        Testing to_dictionary method
        """
        r1 = Rectangle(10, 2, 1, 9)
        self.assertEqual(r1.__str__(), '[Rectangle] (1) 1/9 - 10/2')

        r1_dictionary = r1.to_dictionary()
        expected_result = {'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9}
        self.assertEqual(r1_dictionary, expected_result)
        self.assertTrue(type(r1_dictionary), dict)

        r2 = Rectangle(1, 1)
        self.assertEqual(r2.__str__(), '[Rectangle] (2) 0/0 - 1/1')

        r2.update(**r1_dictionary)
        self.assertEqual(r2.__str__(), '[Rectangle] (1) 1/9 - 10/2')

        self.assertFalse(r1 == r2)

    if __name__ == "__main__":
        unittest.main()
