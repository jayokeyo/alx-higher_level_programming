#!/usr/bin/python3
"""
Defines a function that performs matrix division.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.
    Args:
        matrix: 2-D list of ints or floats.
        div: divisor.
    Raises:
        TypeError: If matrix contains non-real numbers or
                   rows of different sizes or
                   div is not an int or float.
        ZeroDivisionError: If div is 0.
    Returns:
        the result of the division in matrix format
    """

    if (not isinstance(matrix, list) or matrix == [] or \
            not all(isinstance(row, list) for row in matrix) or \
            not all((isinstance(elements, int) \
            or isinstance(elements, float)) for elements in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
