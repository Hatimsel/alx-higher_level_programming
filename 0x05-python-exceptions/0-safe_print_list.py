#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elements_num = 0
    i = 0

    try:
        for i in my_list:
            if elements_num < x:
                print(i, end = '')
                elements_num += 1
            else:
                break
        print()
        return elements_num
    except:
        return elements_num
