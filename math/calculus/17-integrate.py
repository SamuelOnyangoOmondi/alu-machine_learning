#!/usr/bin/env python3
def poly_integral(poly, C=0):
    if not all(isinstance(coef, (int, float)) for coef in poly) or not isinstance(C, (int, float)):
        return None
    
    if not poly:  # if the polynomial is empty, return None
        return None
    
    integral = [C]  # start with the constant of integration
    for i, coef in enumerate(poly):
        if coef == 0:
            integral.append(0)
        else:
            new_coef = coef / (i + 1)
            # if the new coefficient is a whole number, represent it as an integer
            if new_coef.is_integer():
                new_coef = int(new_coef)
            integral.append(new_coef)
    
    # Remove trailing zeros from the list of coefficients
    while len(integral) > 1 and integral[-1] == 0:
        integral.pop()
    
    return integral


# Test the function with the provided example
poly = [5, 3, 0, 1]
print(poly_integral(poly))
