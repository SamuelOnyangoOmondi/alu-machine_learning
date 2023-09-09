#!/usr/bin/env python3

"""
This module provides functionality to concatenate two 2D matrices along a specific axis.
"""

def cat_matrices2D(mat1, mat2, axis=0):
    """Concatenates two matrices along a specific axis."""
    
    # If axis is 0 (vertical concatenation)
    if axis == 0:
        # Check if number of columns is the same in both matrices
        if len(mat1[0]) != len(mat2[0]):
            return None
        return mat1 + mat2

    # If axis is 1 (horizontal concatenation)
    elif axis == 1:
        # Check if number of rows is the same in both matrices
        if len(mat1) != len(mat2):
            return None
        return [row1 + row2 for row1, row2 in zip(mat1, mat2)]
    
    # For any other value of axis, return None
    else:
        return None


# Testing
if __name__ == "__main__":
    mat1 = [[1, 2], [3, 4]]
    mat2 = [[5, 6]]
    mat3 = [[7], [8]]
    mat4 = cat_matrices2D(mat1, mat2)
    mat5 = cat_matrices2D(mat1, mat3, axis=1)
    print(mat4)
    print(mat5)
    
    # Modifying the original matrices to show that the new matrices are independent
    mat1[0] = [9, 10]
    mat1[1].append(5)
    print(mat1)
    print(mat4)
    print(mat5)
