#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

# Define the values of y
y = np.arange(0, 11) ** 3

# Define the x-axis values (0 to 10)
x = np.arange(0, 11)

# Plot y as a solid red line
plt.plot(x, y, 'r-')  # 'r-' specifies a solid red line

# Add labels and a title
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Line Graph of y = x^3')

# Show the plot
plt.show()
