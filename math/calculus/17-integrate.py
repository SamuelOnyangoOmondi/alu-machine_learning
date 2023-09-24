#!/usr/bin/env python3
# Ensure that the poly is correctly initialized
poly = [5, 3, 0, 1]

# Call the function once and print the result
# Ensure there is no extra call to this function with print statement
print(poly_integral(poly))

# If you want to check multiple cases, it should match the expected output
print(poly_integral([0, 7, 2, 2, 0.25, 1]))
print(poly_integral([5, 4, 4, 0.6666666666666666, 1, 1.4, 0.16666666666666666, 1.2857142857142858]))
