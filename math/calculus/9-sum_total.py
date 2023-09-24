#!/usr/bin/env python3
def summation_i_squared(n):
    if not isinstance(n, (int, float)) or n < 1:
        return None
    if isinstance(n, float) and n.is_integer():
        n = int(n)
    return (n * (n + 1) * (2 * n + 1)) // 6
