#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 21000, 1000)
r = np.log(0.5)
t1 = 5730
t2 = 1600
y1 = np.exp((r / t1) * x)
y2 = np.exp((r / t2) * x)

# Create line graphs for y1 and y2
plt.plot(x, y1, 'r--', label='C-14')  # 'r--' specifies a dashed red line for y1
plt.plot(x, y2, 'g-', label='Ra-226')  # 'g-' specifies a solid green line for y2

# Add labels and title
plt.xlabel('Time (years)')
plt.ylabel('Fraction Remaining')
plt.title('Exponential Decay of Radioactive Elements')

# Set the axis ranges
plt.xlim(0, 20000)
plt.ylim(0, 1)

# Place the legend in the upper right-hand corner
plt.legend(loc='upper right')

# Show the plot
plt.show()
