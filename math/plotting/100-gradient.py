#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)

x = np.random.randn(2000) * 10
y = np.random.randn(2000) * 10
z = np.random.rand(2000) + 40 - np.sqrt(np.square(x) + np.square(y))

# Create a scatter plot
fig, ax = plt.subplots(figsize=(8, 6))
scatter = ax.scatter(x, y, c=z, cmap='viridis', marker='.')

# Set labels and title
ax.set_xlabel('x coordinate (m)')
ax.set_ylabel('y coordinate (m)')
ax.set_title('Mountain Elevation')

# Create a colorbar
cbar = plt.colorbar(scatter)
cbar.set_label('Elevation (m)')

# Show the plot
plt.show()
