#!/usr/bin/env python3
"""This module is of a binary classification"""
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
        """Getter for W."""
        return self.__W

    @property
    def b(self):
        """Getter for b."""
        return self.__b

    @property
    def A(self):
        """Getter for A."""
        return self.__A

    def forward_prop(self, X):
        """Add forward propagation (from previous tasks if necessary)"""
        z = np.dot(self.__W, X) + self.__b
        self.__A = 1 / (1 + np.exp(-z))
        return self.__A

    def gradient_descent(self, X, Y, A, alpha=0.05):
        """Performs a single pass of gradient descent on the neuron."""
        m = Y.shape[1]
        dz = A - Y
        dw = np.dot(X, dz.T) / m
        db = np.sum(dz) / m
        self.__W = self.__W - alpha * dw.T
        self.__b = self.__b - alpha * db


# Usage example
if __name__ == "__main__":
    np.random.seed(0)
    neuron = Neuron(784)
    X = np.random.randn(784, 1)  # Example input
    Y = np.array([[1]])          # Example label
    A = neuron.forward_prop(X)
    neuron.gradient_descent(X, Y, A, 0.5)
    print(neuron.W)
    print(neuron.b)
