#!/usr/bin/env python3

def np_elementwise(mat1, mat2):
    """
    Perform element-wise addition, subtraction, multiplication, and division.
    """
    
    # Convert scalar mat2 to matrix form if necessary
    mat2 = [mat2]*len(mat1) if not hasattr(mat2[0], '__len__') else mat2
    
    add = [[i + j for i, j in zip(row1, row2)] for row1, row2 in zip(mat1, mat2)]
    sub = [[i - j for i, j in zip(row1, row2)] for row1, row2 in zip(mat1, mat2)]
    mul = [[i * j for i, j in zip(row1, row2)] for row1, row2 in zip(mat1, mat2)]
    div = [[i / j for i, j in zip(row1, row2)] for row1, row2 in zip(mat1, mat2)]
    
    return add, sub, mul, div

# Given test cases
mat1 = [[11, 22, 33], [44, 55, 66]]
mat2 = [[1, 2, 3], [4, 5, 6]]

print(mat1)
print(mat2)
add, sub, mul, div = np_elementwise(mat1, mat2)
print("Add:\n", add, "\nSub:\n", sub, "\nMul:\n", mul, "\nDiv:\n", div)

add, sub, mul, div = np_elementwise(mat1, [2, 2, 2])
print("Add:\n", add, "\nSub:\n", sub, "\nMul:\n", mul, "\nDiv:\n", div)
