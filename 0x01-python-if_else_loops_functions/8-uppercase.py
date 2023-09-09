#!/usr/bin/python3


def uppercase(str):
    up_str = ""
    for c in range(len(str)):
        if ord(str[c]) > 90:
            up_str += (chr(ord(str[c]) - 32))
        else:
            up_str += (str[c])
    print(up_str)
