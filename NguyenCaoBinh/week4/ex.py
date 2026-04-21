# =================================================================
# WEEK 4: FUNCTIONAL PROGRAMMING IN PYTHON
# =================================================================

# // Exercise 1: Basic Function & Docstrings
# // Create a function that greets a user and describes the current week.
def welcome_message(name, week_number):
    """Prints a formatted welcome message for the study project."""
    print(f"--- Welcome {name}! ---")
    print(f"Current Status: Progressing through Week {week_number}.")

# // Exercise 2: Mathematical Operations & Return Values
# // Calculate the area of a circle: $$Area = \pi \times r^2$$
# // Demonstrate returning a single calculated value.
def calculate_circle_area(radius):
    import math
    if radius < 0:
        return "Error: Radius cannot be negative."
    area = math.pi * (radius ** 2)
    return round(area, 4)

# // Exercise 3: Default Arguments & Keyword Arguments
# // Create a function for a login system with a default 'attempts' value.
def login_system(username, password, attempts=3):
    print(f"User: {username} is attempting to login.")
    print(f"System allows {attempts} attempts before lockout.")

# // Exercise 4: Returning Multiple Values
# // Write a function that returns the minimum, maximum, and sum of three numbers.
def get_stats(a, b, c):
    total = a + b + c
    minimum = min(a, b, c)
    maximum = max(a, b, c)
    return minimum, maximum, total  # Returns a tuple

# // Exercise 5: Variable-length Arguments (*args)
# // Create a function that calculates the average of an unknown number of grades.
def calculate_average(*grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)

# // Exercise 6: Scope Management (Global vs Local)
# // Demonstrate how to modify a global counter from within a function.
execution_count = 0

def increment_execution():
    global execution_count
    execution_count += 1
    print(f"Function executed {execution_count} time(s).")

# // Exercise 7: Lambda Functions
# // Use a lambda to calculate the square of a number for rapid processing.
square_func = lambda x: x**2

# -----------------------------------------------------------------
# EXECUTION AND TESTING
# -----------------------------------------------------------------

# Testing Exercise 1
welcome_message("Cao Binh", 4)

# Testing Exercise 2
print(f"Circle Area (r=5): {calculate_circle_area(5)}")

# Testing Exercise 3 (Mixing positional and keyword arguments)
login_system("admin_hcmut", "P@ssw0rd123", attempts=5)

# Testing Exercise 4 (Unpacking multiple return values)
min_val, max_val, total_sum = get_stats(15, 42, 7)
print(f"Stats -> Min: {min_val}, Max: {max_val}, Sum: {total_sum}")

# Testing Exercise 5
avg = calculate_average(8.5, 9.0, 7.5, 10.0)
print(f"Class average: {avg}")

# Testing Exercise 6
increment_execution()
increment_execution()

# Testing Exercise 7
print(f"Lambda Square of 12: {square_func(12)}")

# =================================================================
# END OF WEEK 4 PRACTICE
# =================================================================