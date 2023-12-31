#!/usr/bin/env python3
"""
This module provides a function to retrieve the shape of a numpy matrix.
"""


def np_shape(matrix):
    """
    Returns the shape of the given matrix.
    Args:
    - matrix (numpy.ndarray): The input matrix.
    Returns:
    - tuple: The shape of the matrix.
    """
    return matrix.shape

# Assuming you receive the numpy arrays from another source
# Commenting out the following lines since you can't use np.array here
# mat1 = np.array([1, 2, 3, 4, 5, 6])
# mat2 = np.array([])
# mat3 = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]],
#                  [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]])

# If you do receive the arrays call the function
# print(np_shape(mat1))
# print(np_shape(mat2))
# print(np_shape(mat3))
