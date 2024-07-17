# Write a Python function that simulates a single neuron with a sigmoid activation function for binary classification, handling multidimensional input features. 
# The function should take a list of feature vectors (each vector representing multiple features for an example), associated true binary labels, and the neuron's weights (one for each feature) and bias as input. 
# It should return the predicted probabilities after sigmoid activation and the mean squared error between the predicted probabilities and the true labels, both rounded to four decimal places.

# Example:
#         input: features = [[0.5, 1.0], [-1.5, -2.0], [2.0, 1.5]], labels = [0, 1, 0], weights = [0.7, -0.4], bias = -0.1
#         output: ([0.4626, 0.4134, 0.6682], 0.3349)
#         Reasoning: For each input vector, the weighted sum is calculated by multiplying each feature by its corresponding weight, adding these up along with the bias, then applying the sigmoid function to produce a probability. 
#         The MSE is calculated as the average squared difference between each predicted probability and the corresponding true label.

import math

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
    # Your code here
    probabilities = []
    for f_i in features:
      x = sum(weight * features for weight, features in zip(weights , f_i)) + bias
      x = 1 / (1 + math.exp(-x))
      x = round(x , 4)
      probabilities.append(x)

    ans = sum((probability - label) ** 2 for probability , label in zip(probabilities, labels))
    ans = ans / len(labels)
    ans = round(ans , 4)
    return probabilities, ans

print(single_neuron_model([[0.5, 1.0], [-1.5, -2.0], [2.0, 1.5]], [0, 1, 0], [0.7, -0.4], -0.1)) #Expected OP - ([0.4626, 0.4134, 0.6682], 0.3349)
print(single_neuron_model([[1, 2], [2, 3], [3, 1]], [1, 0, 1], [0.5, -0.2], 0)) #Expected OP - ([0.525, 0.5987, 0.7858], 0.21)
