#!/usr/bin/python3

""" defines a square by: (based on 4-square.py) """


class Square:
    """ square class """

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
            return

        for i in range(self.__size):
            print('#' * self.__size)
