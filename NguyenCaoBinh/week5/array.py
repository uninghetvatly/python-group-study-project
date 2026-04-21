# =================================================================
# WEEK 5: DATA STRUCTURES - ARRAYS, LISTS, AND TUPLES
# =================================================================

# // Exercise 1: List Initialization and Basic Methods
# // Create a list of engineering subjects and perform CRUD operations.
subjects = ["Digital Design", "Calculus", "Circuit Theory"]
subjects.append("Python Programming")  # Adding to the end
subjects.insert(1, "Physics")          # Inserting at index 1
subjects[2] = "Advanced Calculus"      # Updating an element
print(f"Updated Subjects: {subjects}")

# // Exercise 2: Advanced Slicing
# // Given a list of numbers from 0 to 10, extract specific patterns.
nums = list(range(11)) 
# // Extract elements from index 2 to 8
slice_1 = nums[2:9]
# // Extract every second element (even numbers in this case)
slice_2 = nums[::2]
# // Reverse the list using slicing
reversed_nums = nums[::-1]
print(f"Slices -> Range: {slice_1}, Evens: {slice_2}, Reverse: {reversed_nums}")

# // Exercise 3: Multidimensional Arrays (Matrices)
# // Create a 3x3 identity matrix and access a specific element.
# // This is crucial for Computer Engineering (Signal processing/Linear Algebra).
matrix = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]
# // Access element at Row 2, Column 2 (Index 1, 1)
element = matrix[1][1]
print(f"Matrix Mid-Element: {element}")

# // Exercise 4: List Comprehension
# // Generate a list of squares for all even numbers between 1 and 10.
squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(f"Squares of Evens: {squares}")

# // Exercise 5: Tuples and Immutability
# // Define a constant coordinate (Latitude, Longitude) and demonstrate why it is safe.
hcmut_location = (10.7733, 106.6607)
# // hcmut_location[0] = 11.0  <-- This would trigger a TypeError
print(f"HCMUT Coordinates (Tuple): {hcmut_location}")

# // Exercise 6: List Searching and Statistics
# // Calculate the average grade and find the highest score in a list.
grades = [8.5, 9.0, 7.5, 10.0, 6.5, 9.5]
def analyze_grades(data):
    avg = sum(data) / len(data)
    highest = max(data)
    lowest = min(data)
    return round(avg, 2), highest, lowest

average, top_score, min_score = analyze_grades(grades)
print(f"Results -> Average: {average}, Max: {top_score}, Min: {min_score}")

# // Exercise 7: Nested Loops with Lists
# // Flatten a 2D matrix into a 1D list.
flattened = []
for row in matrix:
    for item in row:
        flattened.append(item)
print(f"Flattened Matrix: {flattened}")

# =================================================================
# END OF WEEK 5 PRACTICE
# =================================================================