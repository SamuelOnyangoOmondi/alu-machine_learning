#!/usr/bin/env python3

def np_elementwise(mat1, mat2):
    """
    Perform element-wise operations on two matrices.

    Args:
    - mat1 (list of lists): First matrix
    - mat2 (list of lists or scalar): Second matrix or scalar

    Returns:
    - tuple: A tuple containing matrices resulting from element-wise sum, difference, product, and quotient
    """

    # Convert mat2 to matrix if scalar
    mat2 = [[mat2 for _ in mat1[0]] for _ in mat1] if isinstance(mat2, (int, float)) else mat2

    # Element-wise operations
    add = list(map(lambda x: list(map(lambda y, z: y + z, x[0], x[1])), zip(mat1, mat2)))
    sub = list(map(lambda x: list(map(lambda y, z: y - z, x[0], x[1])), zip(mat1, mat2)))
    mul = list(map(lambda x: list(map(lambda y, z: y * z, x[0], x[1])), zip(mat1, mat2)))
    div = list(map(lambda x: list(map(lambda y, z: y / z, x[0], x[1])), zip(mat1, mat2)))

    return (add, sub, mul, div)

# Given code
mat1 = [[11, 22, 33], [44, 55, 66]]
mat2 = [[1, 2, 3], [4, 5, 6]]

print(mat1)
print(mat2)
add, sub, mul, div = np_elementwise(mat1, mat2)
print("Add:\n", add, "\nSub:\n", sub, "\nMul:\n", mul, "\nDiv:\n", div)
add, sub, mul, div = np_elementwise(mat1, 2)
print("Add:\n", add, "\nSub:\n", sub, "\nMul:\n", mul, "\nDiv:\n", div)
