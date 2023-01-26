#!/usr/bin/python3
def roman_to_int(roman_string):
    if (roman_string and type(roman_string) is str):
        latin = {'I': 1, 'V': 5, 'X': 10, 'C': 100, 'L': 50, 'D': 500}
        res, crt, cnt = 0, 0, 0
        for nums in reversed(roman_string):
            if nums in roman_string:
                if crt > latin[nums]:
                    res -= latin[nums]
                else:
                    res += latin[nums]
                crt = latin[nums]

        return res

    return 0
