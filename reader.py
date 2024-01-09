# Initialize empty lists for each parameter
from random import *
import numpy as np
from sklearn.linear_model import LinearRegression
param1_list = []
param2_list = []
param3_list = []
param4_list=[]

# Path to your text file
file_path = 'combined.txt'

# Read data from the text file
with open(file_path, 'r') as file:
    # Iterate over each line in the file
    for line in file:
        # Split the line into values using whitespace as the delimiter
        values = line.strip().split()

        # Assuming there are three values in each line
        if len(values) == 3:
            param1_list.append(float(values[0]))  # Convert to the appropriate data type if needed
            param2_list.append(float(values[1]))
            param3_list.append(float(values[2]))
            param4_list.append(float(values[0])/float(1+random()/100))

# Print the lists
print("Parameter 1:", param1_list)
print("Parameter 2:", param2_list)
print("Parameter 3:", param3_list)

import matplotlib.pyplot as plt

independent_variable=param4_list
dependent_variable=param1_list

X = np.array(independent_variable).reshape(-1, 1)
y = np.array(dependent_variable)

# Create a linear regression model
model = LinearRegression()

# Fit the model to the data
model.fit(X, y)

# Get the slope (coefficient) and intercept of the best-fit line
slope = model.coef_[0]
intercept = model.intercept_

# Predict the dependent variable based on the independent variable
predictions = model.predict(X)

# Plot the original data points and the best-fit line
plt.scatter(independent_variable, dependent_variable, label='Data Points')
plt.plot(independent_variable, predictions, color='red', label='Best-fit Line')
plt.xlabel('Independent Variable')
plt.ylabel('Dependent Variable')
plt.title('Linear Regression Example')
plt.legend()
plt.show()

