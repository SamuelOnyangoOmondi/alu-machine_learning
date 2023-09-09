#!/usr/bin/env python3

def np_elementwise(mat1, mat2):
    """Perform element-wise operations on mat1 and mat2"""
    
    def elementwise_operation(x, y, operation):
        return list(map(operation, x, y))
    
    # Transform scalar mat2 to matrix form if needed
    mat2_matrix = [[mat2]*len(mat1[0])]*len(mat1) if not isinstance(mat2[0], list) else mat2

    add = list(map(lambda x, y: elementwise_operation(x, y, lambda a, b: a + b), mat1, mat2_matrix))
    sub = list(map(lambda x, y: elementwise_operation(x, y, lambda a, b: a - b), mat1, mat2_matrix))
    mul = list(map(lambda x, y: elementwise_operation(x, y, lambda a, b: a * b), mat1, mat2_matrix))
    div = list(map(lambda x, y: elementwise_operation(x, y, lambda a, b: a / b), mat1, mat2_matrix))

    return add, sub, mul, div

mat1 = [[11, 22, 33], [44, 55, 66]]
mat2 = [[1, 2, 3], [4, 5, 6]]

print(mat1)
print(mat2)
add, sub, mul, div = np_elementwise(mat1, mat2)
print("Add:\n", add, "\nSub:\n", sub, "\nMul:\n", mul, "\nDiv:\n", div)

add, sub, mul, div = np_elementwise(mat1, 2)
print("Add:\n", add, "\nSub:\n", sub, "\nMul:\n", mul, "\nDiv:\n", div)
