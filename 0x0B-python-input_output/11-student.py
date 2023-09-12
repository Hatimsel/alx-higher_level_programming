#!/usr/bin/python3
"""
Student to json
"""


class Student:
    """
    class Student
    """
    def __init__(self, first_name, last_name, age):
        """
        class Instantiation
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__

    def to_json(self, attrs=None):
        if isinstance(attrs, list):
            if all(isinstance(item, str) for item in attrs):
                dic = {i: self.__dict__[i] for i in attrs if hasattr(self, i)}
                return dic
        return self.__dict__

    def reload_from_json(self, json):
        dic = {setattr(self, k, v) for k, v in json.items()}
