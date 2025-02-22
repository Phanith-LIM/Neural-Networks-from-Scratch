inputs = [1, 2, 3, 2.5]

weights = [
    [0.2, 0.8, -0.5, 1],
    [0.5, -0.91, 0.26, -0.5],
    [-0.26, -0.27, 0.17, 0.87]
]
bias = [2, 3, 0.5]
output = []

for neuron_weight, neuron_bias in zip(weights, bias):
    neuron_output = 0
    
    for n_input, weight in zip(inputs, neuron_weight):
        neuron_output += n_input * weight

    neuron_output += neuron_bias
    output.append(neuron_output)

print(output)