#!/usr/bin/env python3

def operate(r1, r2):
    return (
        list(map(lambda x, y: x + y, r1, r2)),
        list(map(lambda x, y: x - y, r1, r2)),
        list(map(lambda x, y: x * y, r1, r2)),
        list(map(lambda x, y: x / y, r1, r2))
    )

def np_elementwise(mat1, mat2):
    """
    Perform element-wise operations on two matrices.

    Args:
    - mat1 (list of lists): First matrix
    - mat2 (list of lists or scalar): Second matrix or scalar

    Returns:
    - tuple: A tuple containing matrices resulting from element-wise sum, difference, product, and quotient
    """
    
    # Check if mat2 is a scalar
    mat2 = mat2 if isinstance(mat2[0], list) else [[mat2]*len(mat1[0])]*len(mat1)
    
    result = list(zip(*list(map(operate, mat1, mat2))))

    return ([list(item) for item in result[0]],
            [list(item) for item in result[1]],
            [list(item) for item in result[2]],
            [list(item) for item in result[3]])

# Given code
mat1 = [[11, 22, 33], [44, 55, 66]]
mat2 = [[1, 2, 3], [4, 5, 6]]

print(mat1)
print(mat2)
add, sub, mul, div = np_elementwise(mat1, mat2)
print("Add:\n", add, "\nSub:\n", sub, "\nMul:\n", mul, "\nDiv:\n", div)
add, sub, mul, div = np_elementwise(mat1, 2)
print("Add:\n", add, "\nSub:\n", sub, "\nMul:\n", mul, "\nDiv:\n", div)
