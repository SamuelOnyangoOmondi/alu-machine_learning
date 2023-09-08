#!/usr/bin/env python3

"""
This module provides a function to determine the shape of a given matrix.
"""


def matrix_shape(matrix):
    """
    Returns the shape of a matrix as a list of integers.

    Parameters:
    - matrix: The matrix whose shape is to be determined.

    Returns:
    - A list of integers representing the shape of the matrix.
    """
    shape = []
    while type(matrix) is list:  # check if list
        shape.append(len(matrix))
        matrix = matrix[0]  # next dimension
    return shape
