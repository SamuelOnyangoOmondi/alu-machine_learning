#!/usr/bin/env python3

def np_elementwise(mat1, mat2):
    """Perform element-wise operations on mat1 and mat2."""
    
    def operate(x, y, operation):
        return list(map(operation, x, y))

    mat2_broadcast = [operate(row, [mat2]*len(row), lambda a, b: b) if isinstance(mat2, int) else mat2 for row in mat1]

    add = operate(mat1, mat2_broadcast, lambda x, y: operate(x, y, lambda a, b: a + b))
    sub = operate(mat1, mat2_broadcast, lambda x, y: operate(x, y, lambda a, b: a - b))
    mul = operate(mat1, mat2_broadcast, lambda x, y: operate(x, y, lambda a, b: a * b))
    div = operate(mat1, mat2_broadcast, lambda x, y: operate(x, y, lambda a, b: a / b))

    return add, sub, mul, div

mat1 = [[11, 22, 33], [44, 55, 66]]
mat2 = [[1, 2, 3], [4, 5, 6]]

print(mat1)
print(mat2)
add, sub, mul, div = np_elementwise(mat1, mat2)
print("Add:\n", add, "\nSub:\n", sub, "\nMul:\n", mul, "\nDiv:\n", div)

add, sub, mul, div = np_elementwise(mat1, 2)
print("Add:\n", add, "\nSub:\n", sub, "\nMul:\n", mul, "\nDiv:\n", div)
