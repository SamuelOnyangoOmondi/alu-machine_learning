#!/usr/bin/env python3
import numpy as np


class Neuron:
    def __init__(self, nx):
        if type(nx) != int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be positive")

        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """Getter for private attribute __W."""
        return self.__W

    @property
    def b(self):
        """Getter for private attribute __b."""
        return self.__b

    @property
    def A(self):
        """Getter for private attribute __A."""
        return self.__A


# Usage example
if __name__ == "__main__":
    np.random.seed(0)
    neuron = Neuron(784)
    print(neuron.W)
    print(neuron.b)
    print(neuron.A)
    # The following line will raise an AttributeError
    # neuron.A = 10
