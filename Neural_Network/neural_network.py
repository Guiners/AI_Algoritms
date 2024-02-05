import numpy as np
import pandas as pd


def generate_weight(x, y):
    return 2 * np.random.random((x, y)) - 1


def sigmoid_calc(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_der_calc(x):
    return x * (1 - x)


def test(x):
    result = sigmoid_calc(np.dot(x, weight0))
    result = sigmoid_calc(np.dot(result, weight1))
    if result > 0.4:
        value = 1
    else:
        value = 0

    return result, value


# data
inputs = np.array([[0, 0, 1], [1, 1, 1], [0, 1, 1], [1, 0, 1]])

outputs = np.array([[0], [0], [1], [1]])

# seed
np.random.seed(23)

# weights
weight0 = generate_weight(3, 4)
weight1 = generate_weight(4, 1)

for epoch in range(50000):

    layer0 = inputs  # input layer

    layer1 = np.dot(layer0, weight0)  # first layer
    layer1 = sigmoid_calc(layer1)

    layer2 = np.dot(layer1, weight1)  # second layer
    layer2 = sigmoid_calc(layer2)

    layer2_error = outputs - layer2  # comparing output from data with prediction

    if epoch % 10000 == 0:
        error = np.mean(np.abs(layer2_error))
        print("error value:" + str(error))

    layer2_delta = layer2_error * sigmoid_der_calc(
        layer2
    )  # getting info to change weights

    layer1_error = layer2_delta.dot(weight1.T)
    layer1_delta = layer1_error * sigmoid_der_calc(
        layer1
    )  # getting info to change weights

    weight1 += layer1.T.dot(layer2_delta)  # improving weights
    weight0 += layer0.T.dot(layer1_delta)


values = []
predictions = []

for i in inputs:  # getting info for data frame
    res, val = test(i)
    values.append(val)
    predictions.append(res)

data = {
    "Inputs": inputs.tolist(),
    "Output": outputs.tolist(),
    "Network prediction": predictions,
    "Network output": values,
}  # creating dataframe
df = pd.DataFrame(data=data)
print(df)
