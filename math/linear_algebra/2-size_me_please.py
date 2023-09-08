#!/usr/bin/env python3
def matrix_shape(matrix):
    shape = []
    while type(matrix) is list:  # Check if it's still a list (a dimension of the matrix)
        shape.append(len(matrix))
        matrix = matrix[0]  # Dive deeper into the next dimension
    return shape
