#!/usr/bin/env python3
"""This module is of a binary classification"""
import numpy as np


class Neuron:
    def __init__(self, nx):
        # ... (previous implementation)

    # ... (other methods including forward_prop and gradient_descent)

    def train(self, X, Y, iterations=5000, alpha=0.05):
        if not isinstance(iterations, int):
            raise TypeError("iterations must be an integer")
        if iterations <= 0:
            raise ValueError("iterations must be a positive integer")
        if not isinstance(alpha, float):
            raise TypeError("alpha must be a float")
        if alpha <= 0:
            raise ValueError("alpha must be positive")

        for i in range(iterations):
            A = self.forward_prop(X)
            self.gradient_descent(X, Y, A, alpha)
        
        return self.evaluate(X, Y)

    def evaluate(self, X, Y):
        """
        Evaluates the neuron’s predictions.
        Assume this method is already implemented or add it as per your previous tasks.
        """
        A = self.forward_prop(X)
        cost = -1 / Y.shape[1] * np.sum(Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A))
        prediction = A.copy()
        prediction[A < 0.5] = 0
        prediction[A >= 0.5] = 1
        accuracy = np.mean(prediction == Y)
        return prediction, cost

# Usage example is provided in your script
