#!/usr/bin/env python3

import numpy as np


def convolve_grayscale_valid(images, kernel):
    """
    Perform a valid convolution on grayscale images using the given kernel.

    Args:
        images (numpy.ndarray): Input grayscale images with shape (m, h, w).
        kernel (numpy.ndarray): Convolution kernel with shape (fh, fw).

    Returns:
        numpy.ndarray: Convolved images with shape (m, h - fh + 1, w - fw + 1).
    """
    m, h, w = images.shape
    fh, fw = kernel.shape

    h = h - fh + 1
    w = w - fw + 1
    convolution = np.zeros((m, h, w))

    for i in range(h):
        h_start, h_end = i, i + fh
        for j in range(w):
            w_start, w_end = j, j + fw
            images_slice = images[:, h_start:h_end, w_start:w_end]
            convolution[:, i, j] = np.sum(images_slice * kernel, axis=(1, 2))
    return convolution


if __name__ == '__main__':
    # Example usage:
    dataset = np.load('../../supervised_learning/data/MNIST.npz')
    images = dataset['X_train']
    print("Input images shape:", images.shape)
    kernel = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
    images_conv = convolve_grayscale_valid(images, kernel)
    print("Convolved images shape:", images_conv.shape)
