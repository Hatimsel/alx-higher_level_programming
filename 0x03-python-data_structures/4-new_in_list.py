#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list)
    temp_list = my_list[:]
    if idx < 0 or idx >= length:
        return temp_list
    else:
        temp_list[idx] = element
        return temp_list
