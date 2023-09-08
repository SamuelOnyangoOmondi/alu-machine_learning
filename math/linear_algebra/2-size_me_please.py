#!/usr/bin/env python3
def matrix_shape(matrix):
    shape = []
    while type(matrix) is list:#check if list
        shape.append(len(matrix))
        matrix = matrix[0]#next dimension
    return shape
