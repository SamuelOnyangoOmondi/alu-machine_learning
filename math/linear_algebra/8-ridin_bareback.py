#!/usr/bin/env python3

"""
This module provides functionality for multiplying two 2D matrices.
"""


def mat_mul(mat1, mat2):
    """
    Multiplies two 2D matrices.

    Parameters:
    - mat1: First matrix (2D list of ints/floats).
    - mat2: Second matrix (2D list of ints/floats).

    Returns:
    - A new matrix that is the product of mat1 and mat2.
    - If the matrices cannot be multiplied, returns None.
    """
    # Number of columns in mat1 must equal number of rows in mat2
    if len(mat1[0]) != len(mat2):
        return None

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]

    # Populate the result matrix with appropriate values
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                result[i][j] += mat1[i][k] * mat2[k][j]      
    return result


# Testing the function
if __name__ == "__main__":
    mat1 = [[1, 2],
            [3, 4],
            [5, 6]]
    mat2 = [[1, 2, 3, 4],
            [5, 6, 7, 8]]
    print(mat_mul(mat1, mat2))
