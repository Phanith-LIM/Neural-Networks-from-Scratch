import matplotlib.pyplot as plt
import numpy as np
import math

# Define ReLU function with width and bias
def relu(x, width, bias):
  return np.maximum(width * x + bias, 0)

# Generate input values
x = np.linspace(0, 2*math.pi, 100)

# Calculate output values using ReLU function
output_neuron_1 = relu(x, width=6.0, bias=0.0)
output_neuron_2 = relu(output_neuron_1, width=-1.0, bias=0.7)

# Create the plot
plt.figure(figsize=(8, 5))
plt.plot(x, output_neuron_2, label='ReLU')  
plt.xlabel('Input (x)')
plt.ylabel('Output (y)')
plt.title('ReLU Activation Function')
plt.legend() 
plt.show()