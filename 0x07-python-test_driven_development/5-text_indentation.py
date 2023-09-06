#!/usr/bin/python3
"""
text_indentation function
takes a ull text with no indentation
prints a new line at each occurence of '.', '?', ':'
"""


def text_indentation(text):
    """
    ...
    ...
    ...
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    for i in text:
        if i == '.' or i == '?' or i == ':':
            print("{:s}".format(i))
            print("\n\033[1C", end="")
        else:
            print("{:s}".format(i), end="")
