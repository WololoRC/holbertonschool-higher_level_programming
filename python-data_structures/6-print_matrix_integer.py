#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix of integers.
    """

    if (len(matrix) <= 1):
        print()
        return

    for a in matrix:
        cnt = 1
        for b in a:
            cnt += 1

            if (cnt > len(matrix)):
                x = "\n"
            else:
                x = " "

            print("{:d}".format(b), end=x)
