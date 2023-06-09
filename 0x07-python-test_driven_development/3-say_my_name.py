#!/usr/bin/python3
""" Say my name function"""


def say_my_name(first_name, last_name=""):
    """
    Prints my full name.

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Defaults to an empty string.

    Raises:
        TypeError: If `first_name` or `last_name` is not a string.

    Returns:
        None
    """
    if type(first_name) != str:
        raise TypeError('first_name must be a string')
    if type(last_name) != str:
        raise TypeError('last_name must be a string')
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))
    return
