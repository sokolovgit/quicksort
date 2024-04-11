import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Read data from the file
with open("output2.txt", "r") as file:
    lines = file.readlines()

# Initialize lists to store data
array_sizes = []
standard_comparisons = []
median_comparisons = []
multi_comparisons = []

# Parse the data
for line in lines:
    data = line.strip().split(",")
    array_sizes.append(int(data[0]))
    standard_comparisons.append(int(data[1]))
    median_comparisons.append(int(data[2]))
    multi_comparisons.append(int(data[3]))



# Plot the graphs as dots with smaller size and transparency
plt.figure(figsize=(10, 6))
plt.scatter(array_sizes, standard_comparisons, label='Standard', marker='o', s=2.2, alpha=0.3)
plt.scatter(array_sizes, median_comparisons, label='Median', marker='o', s=2.2, alpha=0.3)
plt.scatter(array_sizes, multi_comparisons, label='Multi', marker='o', s=2.2, alpha=0.3)

# Perform linear regression for each dataset
x = np.array(array_sizes).reshape(-1, 1)
lin_reg_standard = LinearRegression().fit(x, standard_comparisons)
lin_reg_median = LinearRegression().fit(x, median_comparisons)
lin_reg_multi = LinearRegression().fit(x, multi_comparisons)

# Plot linear regression lines
plt.plot(array_sizes, lin_reg_standard.predict(x), color='cyan', s=2.2)
plt.plot(array_sizes, lin_reg_multi.predict(x), color='lime', s=2.2)
plt.plot(array_sizes, lin_reg_median.predict(x), color='yellow')

plt.xlabel('Array Size')
plt.ylabel('Number of Comparisons')
plt.title('Comparison Performance with Linear Regression')
plt.legend()
plt.grid(True)
plt.show()
