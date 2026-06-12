#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    prev = 0
    for char in reversed(roman_string):
        val = rom.get(char, 0)
        if val >= prev:
            res += val
        else:
            res -= val
        prev = val
    return res
