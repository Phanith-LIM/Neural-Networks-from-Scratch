import numpy as np
import matplotlib.pyplot as plt

# Define x values for sine function
x = np.array([0, np.pi/2, np.pi, 3*np.pi/2])

# Calculate y values using the sin function
y_sin = np.sin(x)

# Given sequence
y_given = np.array([1, 8, 8, 1])

# Plot the sine function values and the given sequence
plt.plot(x, y_sin, 'o-', label='y = sin(x)', color='blue')
plt.plot(x, y_given, 'x--', label='Given Sequence [1, 8, 8, 1]', color='red')

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Comparison of y = sin(x) and Given Sequence')
plt.legend()

# Show the plot
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.show()
