#!/usr/bin/env python3

"""
Module provides functionality to add two 2D matrices element-wise.
"""


def add_matrices2D(mat1, mat2):
    """
    Adds two 2D matrices element-wise.
    Parameters:
    - mat1: First 2D matrix of ints/floats.
    - mat2: Second 2D matrix of ints/floats.

    Returns:
    - A new matrix representing the sum of the input matrices.
      If matrices are of different shapes, return None.
    """
    # Check if the matrices have the same shape
    if len(mat1) != len(mat2) or any(
        len(row1) != len(row2) for row1, row2 in zip(mat1, mat2)
    ):
        return None

    # Compute the sum of the matrices element-wise
    result = []
    for i in range(len(mat1)):
        result_row = [mat1[i][j] + mat2[i][j] for j in range(len(mat1[i]))]
        result.append(result_row)

    return result


# Testing the function
if __name__ == "__main__":
    mat1 = [[1, 2], [3, 4]]
    mat2 = [[5, 6], [7, 8]]
    print(add_matrices2D(mat1, mat2))
    print(mat1)
    print(mat2)
    print(add_matrices2D(mat1, [[1, 2, 3], [4, 5, 6]]))
