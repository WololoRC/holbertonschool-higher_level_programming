#!/usr/bin/python3
def print_last_digit(number):
    """Prints the last digit of a given number"""

    if number < 0:
        number = number * -1

    print("{}".format(number % 10), end="")
    return number % 10
