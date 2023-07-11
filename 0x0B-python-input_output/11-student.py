#!/usr/bin/python3
"""Student to JSON"""


class Student:
    """class Student"""
    def __init__(self, first_name, last_name, age):
        """instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Student to JSON with filter"""
        if type(attrs) is not list:
            return self.__dict__
        dictionary = dict()
        for attr in attrs:
            if attr in self.__dict__:
                dictionary[attr] = self.__dict__[attr]
        return dictionary

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        self.json = json
        for attr in json:
            self.__dict__[attr] = json[attr]
