#!/usr/bin/env python3
class Exponential:
    def __init__(self, data=None, lambtha=1.):
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = 1 / (sum(data) / len(data))  # Calculate lambtha from data

if __name__ == "__main__":
    # Simulate data using a simple random method (for demonstration)
    import random

    random.seed(0)
    data = [random.expovariate(0.5) for _ in range(100)]
    e1 = Exponential(data)
    print('Lambtha:', e1.lambtha)

    e2 = Exponential(lambtha=2)
    print('Lambtha:', e2.lambtha)
