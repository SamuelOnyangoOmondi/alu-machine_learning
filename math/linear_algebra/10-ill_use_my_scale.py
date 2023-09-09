#!/usr/bin/env python3

def np_shape(matrix):
    """Return the shape of a simulated numpy ndarray using recursion."""
    if not isinstance(matrix, list):
        return ()
    return (len(matrix),) + np_shape(matrix[0]) if matrix else ()

# Test cases
mat1 = [1, 2, 3, 4, 5, 6]
mat2 = []
mat3 = [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]],
        [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]]

print(np_shape(mat1))  # Expected output: (6,)
print(np_shape(mat2))  # Expected output: (0,)
print(np_shape(mat3))  # Expected output: (2, 2, 5)
