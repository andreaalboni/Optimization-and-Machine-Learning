import numpy as np

points = np.random.uniform(0, 1, 1000)
gini_index = np.zeros_like(points)

for i in range(len(points)):
    gini_index[i] = 1 - (points[i])**2 - (1 - points[i])**2

# print(f"Gini index: {gini_index}")
print(f"Mean: {np.mean(gini_index)}")
print(f"Max: {np.max(gini_index)}")
print(f"Min: {np.min(gini_index)}")
print(f"Mean value of the 600 central values: {np.mean(gini_index[200:800])}")