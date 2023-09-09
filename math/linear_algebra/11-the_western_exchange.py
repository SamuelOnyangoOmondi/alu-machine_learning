#!/usr/bin/env python3


def np_transpose(matrix):
    """
    Transposes the given matrix.

    Args:
    - matrix: The input matrix, which is assumed to be a numpy ndarray based on external information.

    Returns:
    - The transposed matrix.
    """
    return matrix.T

# Assuming you receive the numpy arrays from another source
# Commenting out the following lines since you can't use np.array here
# mat1 = np.array([1, 2, 3, 4, 5, 6])
# mat2 = np.array([])
# mat3 = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]],
#                  [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]])

# If you do receive the arrays call the function
# print(np_transpose(mat1))
# print(mat1)
# print(np_transpose(mat2))
# print(mat2)
# print(np_transpose(mat3))
# print(mat3)
