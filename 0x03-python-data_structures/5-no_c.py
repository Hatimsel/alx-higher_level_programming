#!/usr/bin/python3
def no_c(my_string):
    length = len(my_string)
    i = 0
    while i < length:
        if my_string[i] == 'C' or my_string[i] == 'c':
            i += 1
            continue
        else:
            print("{:s}".format(my_string[i]), end = "")
            i += 1
