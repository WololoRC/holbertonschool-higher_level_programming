#!/usr/bin/python3
def multiply_list_map(my_list, number):
    new = [list(map(lambda a: a * number, my_list))]
    return new
