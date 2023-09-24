#!/usr/bin/env python3
def poly_integral(poly, C=0):
    """
    Calculates the integral of a polynomial.
    :param poly: list of coefficients representing a polynomial
    :param C: integer, the integration constant
    :return: list of coefficients representing the integral of the polynomial or None if poly or C are not valid
    """
    # Check if poly and C are valid.
    if not isinstance(poly, list) or not all(isinstance(coef, (int, float)) for coef in poly) or not isinstance(C, (int, float)):
        return None
    
    # Your Implementation Here
    
    # For example, if your implementation is correct,
    # and poly = [5, 3, 0, 1], C = 0
    # The result should be [0, 5, 1.5, 0, 0.25]

    # Return the result
    return result
