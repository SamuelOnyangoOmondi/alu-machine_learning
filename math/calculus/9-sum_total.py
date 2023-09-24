#!/usr/bin/env python3
"""
This module contains a function that calculates
the summation of i^2 from 1 to n
"""


def summation_i_squared(n):
    """
    Calculates the summation of i^2 from 1 to n.
    :param n: stopping condition, must be a valid number
    :type n: int or float
    :return: Integer value of the sum or None if n is not a valid number
    :rtype: int or None
    """
    if not isinstance(n, (int, float)) or n < 1:
        return None
    if isinstance(n, float) and n.is_integer():
        n = int(n)
    return (n * (n + 1) * (2 * n + 1)) // 6
