#!/usr/bin/env python3

def np_elementwise(mat1, mat2):
    """Perform element-wise operations on mat1 and mat2"""
    
    # Handle the scenario where mat2 is just a scalar (like 2) and not a matrix
    if isinstance(mat2, (int, float)):
        mat2 = [[mat2 for _ in row] for row in mat1]

    add = [[row1[i] + row2[i] for i in range(len(row1))] for row1, row2 in zip(mat1, mat2)]
    sub = [[row1[i] - row2[i] for i in range(len(row1))] for row1, row2 in zip(mat1, mat2)]
    mul = [[row1[i] * row2[i] for i in range(len(row1))] for row1, row2 in zip(mat1, mat2)]
    div = [[row1[i] / row2[i] for i in range(len(row1))] for row1, row2 in zip(mat1, mat2)]

    return add, sub, mul, div

mat1 = [[11, 22, 33], [44, 55, 66]]
mat2 = [[1, 2, 3], [4, 5, 6]]

print(mat1)
print(mat2)
add, sub, mul, div = np_elementwise(mat1, mat2)
print("Add:\n", add, "\nSub:\n", sub, "\nMul:\n", mul, "\nDiv:\n", div)

add, sub, mul, div = np_elementwise(mat1, 2)
print("Add:\n", add, "\nSub:\n", sub, "\nMul:\n", mul, "\nDiv:\n", div)
