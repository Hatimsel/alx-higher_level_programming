#!/usr/bin/python3
"""
Tests on Base class
"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

def has_docstring(item):
    """
    Checking if an item has a docstring
    """
    return bool(item.__doc__)

class TestBase(unittest.TestCase):
    """
    class TestBase to test Base class and its methods
    """
    def setUp(self):
        """
        Setting up the private attribute nb_objects
        """
        Base._Base__nb_objects = 0

    def test_module_docstring(self):
        """
        Testing if the module has docstirng
        """
        self.assertTrue(has_docstring(Base))

    def test_basic(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base(12)
        self.assertEqual(b3.id, 12)

        b4 = Base()
        self.assertEqual(b4.id, 3)

    def test_base_with_more_parameter(self):
        """
        Testing Base with more arguments
        """
        with self.assertRaises(TypeError):
            b = Base(5, 4)

    def test_to_json_string(self):
        """
        Testing to_json_string method
        """
        r1 = Rectangle(10, 7, 2, 8)
        r1_dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([r1_dictionary])

        expected_dict = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        expected_jsn_dict = '[\
{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}\
]'
        self.assertEqual(r1_dictionary, expected_dict)
        self.assertTrue(type(r1_dictionary) == dict)
        self.assertEqual(json_dictionary, expected_jsn_dict)
        self.assertTrue(type(json_dictionary) == str)

    def test_to_json_string_with_empty_list(self):
        """
        Testing to_json_string with an empty list
        """
        json_dictionary = Base.to_json_string([])

        self.assertTrue(json_dictionary == '[]')

    def test_to_json_string_with_None(self):
        """
        Testing to_json_string method with None
        """
        json_dictionary = Base.to_json_string(None)

        self.assertTrue(json_dictionary == '[]')
        self.assertTrue(len(json_dictionary) == 2)

    def test_to_json_string_with_no_parameter(self):
        """
        Testing to_json_string method with no arguments
        """
        with self.assertRaises(TypeError):
            Rectangle.to_json_string()

    def test_save_to_file(self):
        """
        Testing save_to_file method
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            content = file.read()

        expected_content = '[\
{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}, \
{"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}\
]'

        self.assertEqual(content, expected_content)

    def test_save_to_file_with_no_parameter(self):
        """
        Testing save_to_file method with no arguments
        """
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_list_is_None(self):
        """
        Testing the save_to_file method with a list is None
        """
        Rectangle.save_to_file(None)

        with open("Rectangle.json", "r") as file:
            content = file.read()

        self.assertEqual(content, '[]')
        self.assertTrue(len(content) == 2)

    def test_from_json_string(self):
        """
        Testing from_json_string method
        """
        list_input = [
                {'id': 89, 'width': 10, 'height': 4},
                {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)

        expected_jsn_lst_inpt = '[\
{"id": 89, "width": 10, "height": 4}, \
{"id": 7, "width": 1, "height": 7}\
]'

        expected_list_output = [
                {'height': 4, 'width': 10, 'id': 89},
                {'height': 7, 'width': 1, 'id': 7}
        ]

        self.assertTrue(type(list_input) == list)
        self.assertTrue(type(json_list_input) == str)
        self.assertTrue(type(list_output) == list)

        self.assertEqual(json_list_input, expected_jsn_lst_inpt)
        self.assertEqual(list_output, expected_list_output)

    def test_from_json_string_None(self):
        """
        Testing from_json_string() with None
        """
        self.assertTrue(Rectangle.from_json_string(None) == [])
        self.assertTrue(Rectangle.from_json_string([]) == [])
        self.assertEqual(Rectangle.from_json_string('[1, 2]'), [1, 2])
        self.assertTrue(Rectangle.from_json_string('{"id": 5}') == {'id': 5})

    def test_from_json_string_with_no_parameter(self):
        """
        Testing from_json_string method with no arguments
        """
        with self.assertRaises(TypeError):
            Rectangle.from_json_string()

    def test_create_method(self):
        """
        Testing create method
        """
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)

        expected_r1_str = '[Rectangle] (1) 1/0 - 3/5'
        expected_r2_str = '[Rectangle] (1) 1/0 - 3/5'

        self.assertEqual(r1.__str__(), expected_r1_str)
        self.assertEqual(r2.__str__(), expected_r2_str)

        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_load_from_file(self):
        """
        Testing load_from_file method
        """
        r1 = Rectangle(10, 7, 2, 8)
        list_rectangles_input = [r1]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()

        for rect in list_rectangles_output:
            expected_result = '[Rectangle] (1) 2/8 - 10/7'
            self.assertEqual(rect.__str__(), expected_result)

    def test_save_to_file_csv(self):
        """
        Testing save_to_file_csv method
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file_csv(list_rectangles_input)
        filename = 'Rectangle.csv'
        with open(filename, 'r', encoding="utf-8") as f:
            content = f.read()

        expected_content = 'id,width,height,x,y\n1,10,7,2,8\n2,2,4,0,0\n'

        self.assertTrue(os.path.exists(filename))
        self.assertEqual(content, expected_content)

    def test_load_from_csv(self):
        """
        Testing load_from_csv method
        """
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]

        Square.save_to_file_csv(list_squares_input)

        list_squares_output = Square.load_from_file_csv()

        self.assertTrue(len(list_squares_output) == 2)
        self.assertFalse(list_squares_output == None)

    if __name__ == "__name__":
        unittest.main()
