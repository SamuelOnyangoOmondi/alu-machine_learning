#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

# Seed for reproducibility
np.random.seed(5)

# Define the fruit matrix
fruit = np.random.randint(0, 20, (4, 3))

# Define the fruit names and colors
fruit_names = ['Apples', 'Bananas', 'Oranges', 'Peaches']
fruit_colors = ['red', 'yellow', '#ff8000', '#ffe5b4']

# Create a stacked bar graph
fig, ax = plt.subplots(figsize=(8, 6))
x = np.arange(3)  # Number of people (Farrah, Fred, Felicia)

# Initialize the bottom for stacking
bottom = np.zeros(3)

# Iterate through each fruit
for i, fruit_name in enumerate(fruit_names):
    fruit_quantity = fruit[i]
    ax.bar(x, fruit_quantity, width=0.5, label=fruit_name, color=fruit_colors[i], bottom=bottom)
    bottom += fruit_quantity

# Set labels and title
ax.set_xlabel('Person')
ax.set_ylabel('Quantity of Fruit')
ax.set_title('Number of Fruit per Person')

# Set the y-axis range and ticks
ax.set_ylim(0, 80)
ax.set_yticks(np.arange(0, 81, 10))

# Set the x-axis labels to Farrah, Fred, and Felicia
ax.set_xticks(x)
ax.set_xticklabels(['Farrah', 'Fred', 'Felicia'])

# Set the legend
ax.legend()

# Show the plot
plt.show()
