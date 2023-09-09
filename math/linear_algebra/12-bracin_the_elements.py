#!/usr/bin/env python3

import numpy as np

def np_elementwise(mat1, mat2):
    """Perform element-wise operations on mat1 and mat2"""
    # Element-wise addition
    add = np.add(mat1, mat2)
    # Element-wise subtraction
    sub = np.subtract(mat1, mat2)
    # Element-wise multiplication
    mul = np.multiply(mat1, mat2)
    # Element-wise division (using numpy's division which handles divide by zero gracefully by returning 'inf')
    div = np.divide(mat1, mat2)
    
    return add, sub, mul, div

mat1 = np.array([[11, 22, 33], [44, 55, 66]])
mat2 = np.array([[1, 2, 3], [4, 5, 6]])

print(mat1)
print(mat2)
add, sub, mul, div = np_elementwise(mat1, mat2)
print("Add:\n", add, "\nSub:\n", sub, "\nMul:\n", mul, "\nDiv:\n", div)

add, sub, mul, div = np_elementwise(mat1, 2)
print("Add:\n", add, "\nSub:\n", sub, "\nMul:\n", mul, "\nDiv:\n", div)
