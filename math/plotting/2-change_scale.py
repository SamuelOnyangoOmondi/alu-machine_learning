#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 28651, 5730)
r = np.log(0.5)
t = 5730
y = np.exp((r / t) * x)

# Create a line graph
plt.plot(x, y, 'b-', label='C-14 Decay')  # 'b-' specifies a blue solid line

# Add labels and title
plt.xlabel('Time (years)')
plt.ylabel('Fraction Remaining')
plt.title('Exponential Decay of C-14')

# Set the y-axis to logarithmic scale
plt.yscale('log')

# Set the x-axis range
plt.xlim(0, 28650)

# Display the legend (if you want)
plt.legend()

# Show the plot
plt.show()
