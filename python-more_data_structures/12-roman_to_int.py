#!/usr/bin/python3
def roman_to_int(roman_string):
    if (roman_string):
        latin = {'I': 1, 'V': 5, 'X': 10, 'C': 100, 'L': 50, 'D': 500}
        arabic = []
        res = 0

        for nums in roman_string:
            if nums in latin:
                arabic.append(latin.get(nums))

        for i in arabic:
            res += i

        return res

    return 0
