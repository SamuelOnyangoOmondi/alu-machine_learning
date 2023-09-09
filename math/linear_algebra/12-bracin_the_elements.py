#!/usr/bin/env python3

def np_elementwise(mat1, mat2):
    """Perform element-wise operations on mat1 and mat2."""
    
    # Assuming the matrices are always 2D
    def operate(row1, row2, operation):
        return list(map(operation, row1, row2))

    mat2_broadcast = mat2 if isinstance(mat2[0], list) else [[mat2] * len(mat1[0])] * len(mat1)

    add = list(map(lambda x, y: operate(x, y, lambda a, b: a + b), mat1, mat2_broadcast))
    sub = list(map(lambda x, y: operate(x, y, lambda a, b: a - b), mat1, mat2_broadcast))
    mul = list(map(lambda x, y: operate(x, y, lambda a, b: a * b), mat1, mat2_broadcast))
    div = list(map(lambda x, y: operate(x, y, lambda a, b: a / b), mat1, mat2_broadcast))

    return add, sub, mul, div

mat1 = [[11, 22, 33], [44, 55, 66]]
mat2 = [[1, 2, 3], [4, 5, 6]]

print(mat1)
print(mat2)
add, sub, mul, div = np_elementwise(mat1, mat2)
print("Add:\n", add, "\nSub:\n", sub, "\nMul:\n", mul, "\nDiv:\n", div)

add, sub, mul, div = np_elementwise(mat1, 2)
print("Add:\n", add, "\nSub:\n", sub, "\nMul:\n", mul, "\nDiv:\n", div)
