#!/usr/bin/env python3
import numpy as np

def convolve_grayscale_valid(images, kernel):
    """
    Perform a valid convolution on grayscale images using the given kernel.

    Args:
        images (numpy.ndarray): Input grayscale images with shape (m, h, w).
        kernel (numpy.ndarray): Convolution kernel with shape (kh, kw).

    Returns:
        numpy.ndarray: Convolved images with shape (m, h - kh + 1, w - kw + 1).
    """
    m, h, w = images.shape
    kh, kw = kernel.shape

    # Calculate the output shape
    out_h = h - kh + 1
    out_w = w - kw + 1

    # Initialize an array to store the convolved images
    convolved_images = np.zeros((m, out_h, out_w), dtype=np.float32)

    # Iterate through each image and perform the convolution
    for i in range(m):
        for j in range(out_h):
            for k in range(out_w):
                # Extract the region from the image
                image_region = images[i, j:j+kh, k:k+kw]
                # Perform element-wise multiplication and sum
                convolved_value = np.sum(image_region * kernel)
                convolved_images[i, j, k] = convolved_value

    return convolved_images

if __name__ == '__main__':
    # Example usage:
    dataset = np.load('../../supervised_learning/data/MNIST.npz')
    images = dataset['X_train']
    print("Input images shape:", images.shape)
    
    kernel = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
    images_conv = convolve_grayscale_valid(images, kernel)
    
    print("Convolved images shape:", images_conv.shape)
