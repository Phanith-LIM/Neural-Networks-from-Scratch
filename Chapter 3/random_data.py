import nnfs
from nnfs.datasets import spiral_data
import matplotlib.pyplot as plt
from dense_layer import Layer_Dense

nnfs.init()

X, y = spiral_data(samples=100, classes=3)

dense1 = Layer_Dense(n_inputs=2, n_neurons=3)
dense1.forward(inputs=X)

# Print the first 5 rows of the output
print(dense1.output[:5])