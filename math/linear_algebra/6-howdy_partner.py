#!/usr/bin/env python3

"""
This module provides a function to concatenate two lists of integers or floats.
"""


def cat_arrays(arr1, arr2):
    """
    Concatenates two lists.

    Parameters:
    - arr1: First list of ints/floats.
    - arr2: Second list of ints/floats.

    Returns:
    - A new list that represents the concatenation of the two input lists.
    """
    return arr1 + arr2


# Testing the function
if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [6, 7, 8]
    print(cat_arrays(arr1, arr2))
    print(arr1)
    print(arr2)
