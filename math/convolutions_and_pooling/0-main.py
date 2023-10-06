import matplotlib.pyplot as plt
import numpy as np
from convolve_grayscale_valid import convolve_grayscale_valid  # Import the function from your implementation

if __name__ == '__main__':
    dataset = np.load('../../supervised_learning/data/MNIST.npz')
    images = dataset['X_train']
    print("Input images shape:", images.shape)

    kernel = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
    images_conv = convolve_grayscale_valid(images, kernel)

    print("Convolved images shape:", images_conv.shape)

    # Display the first original and convolved images for visualization
    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(images[0], cmap='gray')

    plt.subplot(1, 2, 2)
    plt.title("Convolved Image")
    plt.imshow(images_conv[0], cmap='gray')

    plt.show()
