#!/usr/bin/python3

""" size validation """


class Square:
    """ define square """

    def __init__(self, size=0):
        """ inicializing set """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
