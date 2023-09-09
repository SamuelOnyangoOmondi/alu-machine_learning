#!/usr/bin/env python3

def np_elementwise(mat1, mat2):
    """
    Performs element-wise addition, subtraction, multiplication, and division on the given matrices.

    Args:
    - mat1 (List[List[int or float]]): First input matrix.
    - mat2 (List[List[int or float]] or int or float): Second input matrix or scalar value.

    Returns:
    - tuple: A tuple containing the element-wise sum, difference, product, and quotient, respectively.
    """
    
    operation = lambda func, a, b: list(map(lambda x, y: func(x, y), a, b))
    
    add_func = lambda a, b: a + b
    sub_func = lambda a, b: a - b
    mul_func = lambda a, b: a * b
    div_func = lambda a, b: a / b
    
    if isinstance(mat2, (int, float)):
        add = list(map(lambda x: [x + mat2 for x in mat1], mat1))
        sub = list(map(lambda x: [x - mat2 for x in mat1], mat1))
        mul = list(map(lambda x: [x * mat2 for x in mat1], mat1))
        div = list(map(lambda x: [x / mat2 for x in mat1], mat1))
    else:
        add = list(map(lambda x, y: operation(add_func, x, y), mat1, mat2))
        sub = list(map(lambda x, y: operation(sub_func, x, y), mat1, mat2))
        mul = list(map(lambda x, y: operation(mul_func, x, y), mat1, mat2))
        div = list(map(lambda x, y: operation(div_func, x, y), mat1, mat2))

    return add, sub, mul, div

mat1 = [[11, 22, 33], [44, 55, 66]]
mat2 = [[1, 2, 3], [4, 5, 6]]

print(mat1)
print(mat2)
add, sub, mul, div = np_elementwise(mat1, mat2)
print("Add:\n", add, "\nSub:\n", sub, "\nMul:\n", mul, "\nDiv:\n", div)
add, sub, mul, div = np_elementwise(mat1, 2)
print("Add:\n", add, "\nSub:\n", sub, "\nMul:\n", mul, "\nDiv:\n", div)
