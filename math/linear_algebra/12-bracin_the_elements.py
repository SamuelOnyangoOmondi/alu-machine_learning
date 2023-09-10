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
    
    # Element-wise operations using list comprehension
    add = lambda m1, m2: [[i+j for i, j in zip(r1, r2)] for r1, r2 in zip(m1, m2)]
    sub = lambda m1, m2: [[i-j for i, j in zip(r1, r2)] for r1, r2 in zip(m1, m2)]
    mul = lambda m1, m2: [[i*j for i, j in zip(r1, r2)] for r1, r2 in zip(m1, m2)]
    div = lambda m1, m2: [[i/j for i, j in zip(r1, r2)] for r1, r2 in zip(m1, m2)]
    
    # Check if mat2 is a scalar
    mat2 = mat2 if isinstance(mat2[0], list) else [[mat2]*len(mat1[0])]*len(mat1)
    
    return (add(mat1, mat2), sub(mat1, mat2), mul(mat1, mat2), div(mat1, mat2))

# Given code
mat1 = [[11, 22, 33], [44, 55, 66]]
mat2 = [[1, 2, 3], [4, 5, 6]]

print(mat1)
print(mat2)
add, sub, mul, div = np_elementwise(mat1, mat2)
print("Add:\n", add, "\nSub:\n", sub, "\nMul:\n", mul, "\nDiv:\n", div)
add, sub, mul, div = np_elementwise(mat1, 2)
print("Add:\n", add, "\nSub:\n", sub, "\nMul:\n", mul, "\nDiv:\n", div)
