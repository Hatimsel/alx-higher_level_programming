#!/usr/bin/python3
def weight_average(my_list=[]):
    x = []
    wet = 0
    j = 0
    y = 0
    if not my_list:
        return 0
    for lst in my_list:
        for i in range(len(lst)):
            wet += lst[1]
            x.append(lst[0] * lst[1])
    for j in range(len(x)):
        y += x[j]
    y = float(y / wet)
    return y
