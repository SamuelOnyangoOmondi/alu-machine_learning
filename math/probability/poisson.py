#!/usr/bin/env python3
class Poisson:
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
            self.lambtha = float(sum(data) / len(data))

    def poisson_distribution(self, k):
        if k < 0:
            return 0
        from math import exp
        from math import factorial
        return (self.lambtha ** k) * exp(-self.lambtha) / factorial(k)

    def pdf(self, k):
        return self.poisson_distribution(k)

if __name__ == "__main__":
    p1 = Poisson(data=[4, 5, 6, 7, 8])
    print('Lambtha:', p1.lambtha)

    p2 = Poisson(lambtha=5)
    print('Lambtha:', p2.lambtha)
