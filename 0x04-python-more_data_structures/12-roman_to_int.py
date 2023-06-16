#!/usr/bin/python3
def roman_to_int(roman_string):
    rom_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M':1000}
    rt = 0
    if not roman_string:
        return 0
    for i in range(len(roman_string)):
        for key in rom_dict:
            if roman_string[i] == key:
                rt += int(rom_dict[key])
    return rt
