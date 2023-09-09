#!/usr/bin/env python3

def operate_elementwise(a, b, operation):
    return list(map(lambda x, y: operation(x, y), a, b))

def np_elementwise(mat1, mat2):
    """Perform element-wise operations on mat1 and mat2"""

    # Assuming that if mat2 is a scalar, it has the same length and shape as mat1
    mat2 = mat2 if isinstance(mat2[0], list) else [[mat2]*len(mat1[0])]*len(mat1)

    add = operate_elementwise(mat1, mat2, lambda x, y: list(map(lambda a, b: a + b, x, y)))
    sub = operate_elementwise(mat1, mat2, lambda x, y: list(map(lambda a, b: a - b, x, y)))
    mul = operate_elementwise(mat1, mat2, lambda x, y: list(map(lambda a, b: a * b, x, y)))
    div = operate_elementwise(mat1, mat2, lambda x, y: list(map(lambda a, b: a / b, x, y)))

    return add, sub, mul, div

mat1 = [[11, 22, 33], [44, 55, 66]]
mat2 = [[1, 2, 3], [4, 5, 6]]

print(mat1)
print(mat2)
add, sub, mul, div = np_elementwise(mat1, mat2)
print("Add:\n", add, "\nSub:\n", sub, "\nMul:\n", mul, "\nDiv:\n", div)

add, sub, mul, div = np_elementwise(mat1, 2)
print("Add:\n", add, "\nSub:\n", sub, "\nMul:\n", mul, "\nDiv:\n", div)
