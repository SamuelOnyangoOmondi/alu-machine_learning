#!/usr/bin/env python3

import numpy as np

def np_cat(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a specific axis.
    
    Args:
    - mat1 (numpy.ndarray): First matrix
    - mat2 (numpy.ndarray): Second matrix
    - axis (int, optional): Axis along which to concatenate. Defaults to 0.
    
    Returns:
    - numpy.ndarray: A new matrix resulting from the concatenation
    """
    return np.concatenate((mat1, mat2), axis=axis)

# Testing the function
mat1 = np.array([[11, 22, 33], [44, 55, 66]])
mat2 = np.array([[1, 2, 3], [4, 5, 6]])
mat3 = np.array([[7], [8]])

print(np_cat(mat1, mat2))        # Default is axis=0
print(np_cat(mat1, mat2, axis=1))
print(np_cat(mat1, mat3, axis=1))
