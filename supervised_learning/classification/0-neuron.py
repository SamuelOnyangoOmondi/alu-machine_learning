#!/usr/bin/env python3
import numpy as np


class Neuron:
    """
    Represents a single neuron performing binary classification.

    Attributes:
    W (numpy.ndarray): The weights vector for the neuron. Initialized with a random normal distribution.
    b (float): The bias for the neuron. Initialized to 0.
    A (int): The activated output of the neuron (prediction). Initialized to 0.

    Methods:
    __init__(self, nx): Initializes the neuron with nx input features.
    """
    def __init__(self, nx):
        if type(nx) != int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")

        self.W = np.random.randn(1, nx)
        self.b = 0
        self.A = 0


# Usage example
if __name__ == "__main__":
    np.random.seed(0)
    neuron = Neuron(784)
    print(neuron.W)
    print(neuron.W.shape)
    print(neuron.b)
    print(neuron.A)
    neuron.A = 10
    print(neuron.A)
