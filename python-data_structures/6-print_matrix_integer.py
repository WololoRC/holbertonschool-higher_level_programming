#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix of integers.
    """

    for a in matrix:
        if (len(a) < 1):
            print()
            break
        cnt = 1
        for b in a:
            cnt += 1

            if (cnt > len(a)):
                x = "\n"
            else:
                x = " "

            print("{:d}".format(b), end=x)
