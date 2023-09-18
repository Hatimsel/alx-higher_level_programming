#!/usr/bin/python3
"""
Base class
"""
import json
import csv
import turtle


class Base:
    """
    Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Instantiation of the class Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON representation of a list of dictionaries
        """
        empty = "[]"

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return empty

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file
        """
        filename = cls.__name__ + ".json"

        if list_objs is None:
            list_objs = []

        list_dicts = [cls.to_dictionary(obj) for obj in list_objs]
        # list_dicts = [
        #         {k.lstrip('_' + cls.__name__): v
        #          for k, v in obj.__dict__.items()}
        #         for obj in list_objs
        #         ]

        with open(filename, 'w', encoding="utf-8") as f:
            f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string
        """
        empty = []

        if json_string is None or len(json_string) == 0:
            return empty

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set
        """
        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ == 'Rectangle':
            dummy = Rectangle(2, 4)
        else:
            dummy = Square(3)

        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances
        """
        import os

        list_of_instances = []
        filename = cls.__name__ + '.json'

        if os.path.exists(filename):
            with open(filename, 'r', encoding="utf-8") as f:
                content = f.read()

            content = cls.from_json_string(content)

            for dic in content:
                list_of_instances.append(cls.create(**dic))

            return list_of_instances

        return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes Python objects into CSV files
        """
        filename = cls.__name__ + '.csv'
        list_of_val = [[], []]
        cls_names = ['Rectangle', 'Square']

        if cls.__name__ == cls_names[0]:
            header = ['id', 'width', 'height', 'x', 'y']

        elif cls.__name__ == cls_names[1]:
            header = ['id', 'size', 'x', 'y']

        data = [cls.to_dictionary(obj) for obj in list_objs]

        with open(filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writeheader()
            writer.writerows(data)

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes a csv into Python objects
        """
        filename = cls.__name__ + '.csv'
        instances = []

        with open(filename, 'r', encoding="utf-8", newline='') as f:
            content = csv.DictReader(f)
            for row in content:
                instance = cls(1, 2)

                row = {k: int(v) for k, v in row.items()}
                instance.update(**row)

                instances.append(instance)

        return instances

    def draw(list_rectangles, list_squares):
        """
        Drawing all the rectangles and square passed in the lists
        """
        rectangle = turtle.Turtle()
        rectangle.color('blue')
        rectangle.pensize(5)
        rectangle.penup()

        for rect in list_rectangles:
            rect = rect.to_dictionary()
            x = rect['width']
            y = rect['height']
            rectangle.pendown()
            rectangle.speed(1)
            rectangle.fillcolor("blue")
            rectangle.begin_fill()
            rectangle.forward(x)
            rectangle.left(90)
            rectangle.forward(y)
            rectangle.left(90)
            rectangle.forward(x)
            rectangle.left(90)
            rectangle.forward(y)
            rectangle.end_fill()
            rectangle.penup()
            rectangle.forward(200)

        square = turtle.Turtle()
        square.color('green')
        square.pensize(5)
        square.penup()
        square.forward(400)

        for sqr in list_squares:
            sqr = sqr.to_dictionary()
            x = sqr['size']
            square.pendown()
            square.fillcolor("green")
            square.speed(1)
            square.begin_fill()
            square.forward(x)
            square.left(90)
            square.forward(x)
            square.left(90)
            square.forward(x)
            square.left(90)
            square.forward(x)
            square.end_fill()
            square.penup()
            square.forward(200)
