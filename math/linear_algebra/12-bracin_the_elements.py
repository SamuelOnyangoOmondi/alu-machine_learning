#!/usr/bin/env python3

import numpy as np

def np_elementwise(mat1, mat2):
    """
    Performs element-wise addition, subtraction, multiplication, and division on the given matrices.

    Args:
    - mat1 (numpy.ndarray): First input matrix.
    - mat2 (numpy.ndarray or int or float): Second input matrix or scalar value.

    Returns:
    - tuple: A tuple containing the element-wise sum, difference, product, and quotient, respectively.
    """
    add = mat1 + mat2
    sub = mat1 - mat2
    mul = mat1 * mat2
    div = mat1 / mat2
    return add, sub, mul, div

mat1 = np.array([[11, 22, 33], [44, 55, 66]])
mat2 = np.array([[1, 2, 3], [4, 5, 6]])

print(mat1)
print(mat2)
add, sub, mul, div = np_elementwise(mat1, mat2)
print("Add:\n", add, "\nSub:\n", sub, "\nMul:\n", mul, "\nDiv:\n", div)
add, sub, mul, div = np_elementwise(mat1, 2)
print("Add:\n", add, "\nSub:\n", sub, "\nMul:\n", mul, "\nDiv:\n", div)
