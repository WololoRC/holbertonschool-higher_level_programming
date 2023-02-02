#!/usr/bin/python3
"""
2-matrix_divided this module only have matrix_divided function
"""


def matrix_divided(matrix, div):
    """return a new matrix with the values of the last / 2

    Parameters
    ----------
    matrix : list, int, float
        a list of list with int or float values.
    div: int, float
        a int or float to divide elements of matrix

    Raises
    ------
    TypeError
        if @div != int or float
        if @matrix is not a list
        if len @matrix[1] != len(rows] of @matrix

    ZeroDivisionError
        if div == 0


    """

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")

    if type(matrix) == list:
        check_lenght = len(matrix[0])
        new = []

        for a in matrix:
            if len(a) != check_lenght:
                raise TypeError("Each row of the matrix"
                                " must have the same size")
            else:
                try:
                    new.append(list(map(lambda x: round(x / div, 2), a)))
                except TypeError:
                    raise ("matrix must be a matrix "
                           "(list of lists) of integers/floats")
                    exit()
                except ZeroDivisionError:
                    raise ZeroDivisionError("division by zero")
                    exit()

    else:
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    return new
