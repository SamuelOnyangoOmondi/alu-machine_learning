#!/usr/bin/env python3

"""
This module has the method that performs
convolution on grayscale images with channels
"""
import numpy as np


def convolve_channels(images, kernel, padding='same', stride=(1, 1)):
    """
    convolution with channels
    """
    m, h, w, c = images.shape
    kh, kw, kc = kernel.shape
    # stride
    sh, sw = stride

    if padding == 'same':
        nh, nw = h, w
        ph  = int((fh + (sh * (h - 1)) - h) / 2 + 0.5)
        pw  = int((fw + (sw * (w - 1)) - w) / 2 + 0.5)
        images = np.pad(images, ((0, 0), (ph, ph), (pw, pw), (0, 0)), 'constant')
    elif padding == 'valid':
        nh = ((h - fh) // sh) + 1
        nw = ((w - fw) // sw) + 1
    else:
        ph, pw = padding
        nh = ((h - fh + (2 * ph)) // sh) + 1
        nw = ((w - fw + (2 * pw)) // sw) + 1

    # output
    out_h = int((h - kh + 2 * ph) / sh) + 1
    out_w = int((w - kw + 2 * pw) / sw) + 1

    # Pad the input images
    images_padded = np.pad(
        images, ((0, 0), (ph, ph), (pw, pw), (0, 0)), mode='constant')

    # initialise convolved images
    convolved_images = np.zeros((m, out_h, out_w))

    # Perform the convolution
    for i in range(out_h):
        for j in range(out_w):
            # Extract a patch from the image
            patch = images_padded[:, i * sh:i * sh + kh, j * sw:j * sw + kw, :]
            convolved_images[:, i, j] = np.tensordot(
                patch, kernel, axes=([1, 2, 3], [0, 1, 2]))

    return convolved_images
