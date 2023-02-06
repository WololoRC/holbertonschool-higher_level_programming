#!/usr/bin/python3
def square_matrix_simple(matrix):
    """
    computes the square value of all integers of a matrix.
    """
    
    square = []

    for i in matrix:
        square.append(list(map(lambda x: x ** 2, i)))

    return square
