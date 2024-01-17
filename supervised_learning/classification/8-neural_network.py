#!/usr/bin/env python3
import numpy as np


class NeuralNetwork:
    def __init__(self, nx, nodes):
        if type(nx) != int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if type(nodes) != int:
            raise TypeError("nodes must be an integer")
        if nodes < 1:
            raise ValueError("nodes must be a positive integer")

        self.W1 = np.random.randn(nodes, nx)
        self.b1 = np.zeros((nodes, 1))
        self.A1 = 0
        self.W2 = np.random.randn(1, nodes)
        self.b2 = 0
        self.A2 = 0

# Usage example
if __name__ == "__main__":
    np.random.seed(0)
    nn = NeuralNetwork(784, 3)
    print(nn.W1)
    print(nn.W1.shape)
    print(nn.b1)
    print(nn.W2)
    print(nn.W2.shape)
    print(nn.b2)
    print(nn.A1)
    print(nn.A2)
    nn.A1 = 10  # This will work but it's generally not good practice to modify attributes directly
    print(nn.A1)
