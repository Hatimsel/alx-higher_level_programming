#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    length = len(my_list)
    result_list = my_list
    i = 0
    while i < length:
        if my_list[i] % 2 == 0:
            result_list[i] = True
        else:
            result_list[i] = False
        i += 1
    return result_list
