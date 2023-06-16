#!/usr/bin/python3
def roman_to_int(roman_string):
    rom_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M':1000}
    prev_value = 0
    result = 0
    if not roman_string or not str(roman_string):
        return 0
    for char in reversed(roman_string):
        value = rom_dict[char]
        if value >= prev_value:
            result += value
            prev_value = value
        else:
            result -= value
            prev_value = value
    return result
