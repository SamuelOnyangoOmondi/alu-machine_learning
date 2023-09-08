#!/usr/bin/env python3
"""
This module provides functionality to add two arrays element-wise.
"""

def add_arrays(arr1, arr2):
    """
    Adds two arrays element-wise.
    
    Parameters:
    - arr1: First list of ints/floats.
    - arr2: Second list of ints/floats.

    Returns:
    - A new list that represents the sum of the two input lists element-wise.
      If the input lists are of different lengths, return None.
    """
    if len(arr1) != len(arr2):
        return None
    return [a + b for a, b in zip(arr1, arr2)]


# Testing the function
if __name__ == "__main__":
    arr1 = [1, 2, 3, 4]
    arr2 = [5, 6, 7, 8]
    print(add_arrays(arr1, arr2))
    print(arr1)
    print(arr2)
    print(add_arrays(arr1, [1, 2, 3]))
