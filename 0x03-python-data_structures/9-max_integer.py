#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if length == 0:
        return None
    max_int = my_list[0]
    i = 1
    while i < length:
        if max_int < my_list[i]:
            max_int = my_list[i]
        i += 1
    return max_int
