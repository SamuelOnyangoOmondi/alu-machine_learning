#!/usr/bin/env python3

def np_elementwise(mat1, mat2):
    """Perform element-wise operations on mat1 and mat2."""
    
    # Broadcasting mat2 if it's a scalar.
    mat2_broadcast = [[mat2] * len(mat1[0])] * len(mat1)

    add = list(map(lambda x, y: list(map(lambda a, b: a + b, x, (y if isinstance(mat2[0], list) else mat2_broadcast))), mat1, mat2))
    sub = list(map(lambda x, y: list(map(lambda a, b: a - b, x, (y if isinstance(mat2[0], list) else mat2_broadcast))), mat1, mat2))
    mul = list(map(lambda x, y: list(map(lambda a, b: a * b, x, (y if isinstance(mat2[0], list) else mat2_broadcast))), mat1, mat2))
    div = list(map(lambda x, y: list(map(lambda a, b: a / b, x, (y if isinstance(mat2[0], list) else mat2_broadcast))), mat1, mat2))

    return add, sub, mul, div

mat1 = [[11, 22, 33], [44, 55, 66]]
mat2 = [[1, 2, 3], [4, 5, 6]]

print(mat1)
print(mat2)
add, sub, mul, div = np_elementwise(mat1, mat2)
print("Add:\n", add, "\nSub:\n", sub, "\nMul:\n", mul, "\nDiv:\n", div)

add, sub, mul, div = np_elementwise(mat1, 2)
print("Add:\n", add, "\nSub:\n", sub, "\nMul:\n", mul, "\nDiv:\n", div)
