# =================================================================
# WEEK 7: LIBRARY OF CHOICE - NUMPY FOR ENGINEERS
# =================================================================
import numpy as np
import time

# // Exercise 1: Array Creation and Performance Comparison
# // Compare the speed of adding two large lists vs two NumPy arrays.
size = 1000000
list1 = list(range(size))
list2 = list(range(size))

start_time = time.time()
result_list = [x + y for x, y in zip(list1, list2)]
print(f"List Addition Time: {time.time() - start_time:.5f}s")

arr1 = np.arange(size)
arr2 = np.arange(size)
start_time = time.time()
result_arr = arr1 + arr2  # // Vectorized addition
print(f"NumPy Addition Time: {time.time() - start_time:.5f}s")

# // Exercise 2: Matrix Operations (Linear Algebra)
# // Create a 3x3 matrix and perform a dot product.
# // This is common in calculating node voltages in complex circuits.
matrix_a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_b = np.eye(3) # // Creates a 3x3 Identity Matrix

# // Matrix Multiplication (Dot Product)
product = np.dot(matrix_a, matrix_b)
print(f"Matrix A * I:\n{product}")

# // Exercise 3: Reshaping and Slicing
# // Create a 1D array of 12 elements and reshape it into a 3x4 matrix.
data = np.linspace(0, 100, 12) # // 12 linearly spaced points from 0 to 100
grid = data.reshape(3, 4)
print(f"Reshaped 3x4 Grid:\n{grid}")

# // Access the second column of all rows
second_column = grid[:, 1]
print(f"Second Column: {second_column}")

# // Exercise 4: Statistical Analysis
# // Generate random sensor data (e.g., current readings) and find noise levels.
# // np.random.normal(mean, std_dev, size)
current_readings = np.random.normal(5.0, 0.2, 100) 
print(f"Mean Reading: {np.mean(current_readings):.2f}A")
print(f"Max Spike: {np.max(current_readings):.2f}A")
print(f"Standard Deviation (Noise): {np.std(current_readings):.2f}")

# // Exercise 5: Universal Functions (ufuncs)
# // Apply a trigonometric function to an entire array of angles.
angles = np.array([0, 30, 45, 60, 90])
radians = np.radians(angles) # // Convert degrees to radians
sine_values = np.sin(radians)
print(f"Sine values of {angles} degrees:\n{sine_values}")

# // Exercise 6: Filtering Data (Boolean Indexing)
# // Find all values in an array that exceed a certain threshold.
# // Useful for detecting over-voltage or over-current in a system.
voltages = np.array([1.2, 3.3, 5.5, 0.8, 12.1, 4.4])
critical_events = voltages[voltages > 5.0]
print(f"Critical Voltage Events (>5V): {critical_events}")

# =================================================================
# END OF WEEK 7 PRACTICE
# =================================================================