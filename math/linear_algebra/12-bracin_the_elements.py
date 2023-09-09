#!/usr/bin/env python3

def elementwise_operation(op, mat1, mat2):
    if isinstance(mat2, (int, float)):  # Check if mat2 is a scalar
        return list(map(lambda row: list(map(op, row, [mat2]*len(row))), mat1))
    return list(map(lambda row1, row2: list(map(op, row1, row2)), mat1, mat2))

def np_elementwise(mat1, mat2):
    """
    Perform element-wise addition, subtraction, multiplication, and division.
    """
    add = elementwise_operation(lambda x, y: x + y, mat1, mat2)
    sub = elementwise_operation(lambda x, y: x - y, mat1, mat2)
    mul = elementwise_operation(lambda x, y: x * y, mat1, mat2)
    div = elementwise_operation(lambda x, y: x / y, mat1, mat2)
    
    return add, sub, mul, div

# Given test cases
mat1 = [[11, 22, 33], [44, 55, 66]]
mat2 = [[1, 2, 3], [4, 5, 6]]

print(mat1)
print(mat2)
add, sub, mul, div = np_elementwise(mat1, mat2)
print("Add:\n", add, "\nSub:\n", sub, "\nMul:\n", mul, "\nDiv:\n", div)

add, sub, mul, div = np_elementwise(mat1, 2)
print("Add:\n", add, "\nSub:\n", sub, "\nMul:\n", mul, "\nDiv:\n", div)
