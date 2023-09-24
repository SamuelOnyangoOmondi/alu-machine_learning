#!/usr/bin/env python3
"""
Module for calculating the derivative of a polynomial.
The polynomial is represented as a list of coefficients,
where the index of each coefficient corresponds to the power of x.
"""

def poly_derivative(poly):
    """
    Calculates the derivative of a polynomial.
    
    :param poly: List of coefficients representing a polynomial
                 The index of the list represents the power of x that the coefficient belongs to
    :type poly: list
    :return: New list of coefficients representing the derivative of the polynomial
    :rtype: list or None
    """
    if not isinstance(poly, list) or len(poly) == 0 or not all(isinstance(coef, (int, float)) for coef in poly):
        return None

    if len(poly) == 1:
        return [0]  # the derivative of a constant is 0
    
    derivative = [poly[i] * i for i in range(1, len(poly))]
    
    return derivative
