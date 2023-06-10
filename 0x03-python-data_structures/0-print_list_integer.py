#!/usr/bin/python3
def print_list_integer(my_list=[]):
    length = len(my_list)
    i = 0
    while i <= length - 1:
        print("{}".format(my_list[i]))
        i += 1
        if length > 0:
            print("{}".format(my_list[length - 1]), end= "\r")
