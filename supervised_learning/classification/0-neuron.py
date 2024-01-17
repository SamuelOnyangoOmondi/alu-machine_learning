#!/usr/bin/env python3
"""
This module defines the Neuron class for binary classification. The Neuron class
represents a single neuron with capabilities to perform binary classification tasks.
It includes initialization of weights, bias, and activation output based on the number
of input features provided.
"""

import numpy as np


class Neuron:
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
