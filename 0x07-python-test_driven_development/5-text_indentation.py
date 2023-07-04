#!/usr/bin/python3
""" text_indentation function"""


def text_indentation(text):
    """Prints the text with 2 new lines after ., ?, and : characters"""
    if type(text) != str:
        raise TypeError('text must be a string')
    text = text.strip()
    for i in range(len(text)):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print(text[i])
            print()
        else:
            if text[i] != ' ' or (i > 0 and text[i-1] not in ('.', '?', ':')):
                print(text[i], end="")
