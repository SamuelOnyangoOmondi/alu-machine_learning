#!/usr/bin/env python3

# Importing the poly_integral function from the 17-integrate module
from 17-integrate import poly_integral

poly = [5, 3, 0, 1]  # example poly

# Printing the result
print(poly_integral(poly, C=0))  # Replace C=0 with your integration constant if different

# Additional test cases
print(poly_integral([0, 7, 2, 2, 0.25, 1], C=1))
print(poly_integral([5, 4, 4, 0.6666666666666666, 1, 1.4, 0.16666666666666666, 1.2857142857142858], C=0))
