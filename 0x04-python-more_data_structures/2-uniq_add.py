#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_nums = []
    result = 0
    for num in my_list:
        if num not in unique_nums:
            unique_nums.append(num)
            result += num
    return result
