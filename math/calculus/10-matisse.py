#!/usr/bin/env python3
def poly_derivative(poly):
    """
    Calculates the derivative of a polynomial.

    :param poly: List of coefficients representing a polynomial.
    Index of the list represents the power of x.
    :type poly: list
    :return: New list of coefficients for coefficients.
    :rtype: list or None
    """
    if not isinstance(poly, list) or len(poly) == 0 or not all(
        isinstance(coef, (int, float)) for coef in poly
    ):
        return None

    if len(poly) == 1:
        return [0]  # the derivative of a constant is 0

    derivative = [poly[i] * i for i in range(1, len(poly))]

    return derivative
