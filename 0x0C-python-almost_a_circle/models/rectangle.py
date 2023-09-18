#!/usr/bin/python3
"""
First Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    class Rectangle inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Instantiation of the class
        """
        args = {"width": width, "height": height, "x": x, "y": y}
        for k, v in args.items():
            if type(args[k]) is not int:
                raise TypeError(f'{k} must be an integer')

        if width <= 0:
            raise ValueError('width must be > 0')

        if height <= 0:
            raise ValueError('height must be > 0')

        if x < 0:
            raise ValueError('x must be >= 0')

        if y < 0:
            raise ValueError('y must be >= 0')
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError('width must be an integer')

        if width <= 0:
            raise ValueError('width must be > 0')

        self.__width = width

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError('height must be an integer')

        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @x.setter
    def x(self, x):
        if type(x) != int:
            raise TypeError('x must be an integer')

        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @y.setter
    def y(self, y):
        if type(y) != int:
            raise TypeError('y must be an integer')

        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        """
        returns the area value of the Rectangle instance
        """
        return self.__width * self.__height

    def display(self):
        """
        prints the Rectangle instance with # in stdout
        """
        for j in range(self.__y):
            print()
        for i in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        """
        returns a formatted representation of the class Rectangle
        """
        a, b, c = self.id, self.__x, self.__y
        return f'[Rectangle] ({a}) {b}/{c} - {self.__width}/{self.__height}'

    def update(self, *args, **kwargs):
        """
        Updates the class Rectangle
        """
        if len(args) > 0:
            attribute_names = ('id', 'width', 'height', 'x', 'y')

            for i, arg in enumerate(args):
                if i >= len(attribute_names):
                    break
                setattr(self, attribute_names[i], arg)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """
        returns a dictionary representation of the Rectangle class
        """
        # Tricking pycodestyle
        a, b, c = 'id', 'width', 'height'
        f, g, h = self.id, self.__width, self.__height
        dic = {a: f, b: g, c: h, 'x': self.__x, 'y': self.__y}
        return dic
