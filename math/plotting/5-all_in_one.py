#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

# Define y0
y0 = np.arange(0, 11) ** 3

# Create a 3x2 grid of subplots
fig, axes = plt.subplots(3, 2, figsize=(10, 10))

# Set font size for axis labels and titles
font_size = 'x-small'

# First Subplot: Line Graph (y0)
axes[0, 0].plot(np.arange(0, 11), y0, 'r-')
axes[0, 0].set_xlabel('Time (years)', fontsize=font_size)
axes[0, 0].set_ylabel('Fraction Remaining', fontsize=font_size)
axes[0, 0].set_title('Exponential Decay of C-14', fontsize=font_size)

# Second Subplot: Scatter Plot (x1, y1)
mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

axes[0, 1].scatter(x1, y1, c='m', marker='.', label='Data')
axes[0, 1].set_xlabel('Height (in)', fontsize=font_size)
axes[0, 1].set_ylabel('Weight (lbs)', fontsize=font_size)
axes[0, 1].set_title("Men's Height vs Weight", fontsize=font_size)
axes[0, 1].legend(loc='upper right', fontsize=font_size)

# Third Subplot: Line Graph (x2, y2, log scale)
x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

axes[1, 0].plot(x2, y2, 'b-')
axes[1, 0].set_xlabel('Time (years)', fontsize=font_size)
axes[1, 0].set_ylabel('Fraction Remaining', fontsize=font_size)
axes[1, 0].set_title('Exponential Decay of C-14 (Log Scale)', fontsize=font_size)
axes[1, 0].set_yscale('log')

# Fourth Subplot: Line Graph (x3, y31 and y32)
x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

axes[1, 1].plot(x3, y31, 'r--', label='C-14')
axes[1, 1].plot(x3, y32, 'g-', label='Ra-226')
axes[1, 1].set_xlabel('Time (years)', fontsize=font_size)
axes[1, 1].set_ylabel('Fraction Remaining', fontsize=font_size)
axes[1, 1].set_title('Exponential Decay of Radioactive Elements', fontsize=font_size)
axes[1, 1].legend(loc='upper right', fontsize=font_size)

# Fifth Subplot: Histogram (student_grades)
np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

axes[2, 0].hist(student_grades, bins=range(0, 101, 10), edgecolor='black')
axes[2, 0].set_xlabel('Grades', fontsize=font_size)
axes[2, 0].set_ylabel('Number of Students', fontsize=font_size)
axes[2, 0].set_title('Project A', fontsize=font_size)

# Remove the sixth (empty) subplot
fig.delaxes(axes[2, 1])

# Adjust spacing between subplots
plt.tight_layout()

# Set the overall title for the figure
fig.suptitle('All in One', fontsize=font_size)

# Display the plot
plt.show()
