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
    convolved_images = np.zeros((m, h - kh + 1, w - kw + 1), dtype=np.float32)

    for i in range(m):
        for j in range(h - kh + 1):
            for k in range(w - kw + 1):
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
