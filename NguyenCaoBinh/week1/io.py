# ==============================
# Taking Input in Python
# ==============================

print("=== Taking Input ===")

name = input("Enter your name: ")
print("Hello,", name, "! Welcome!")


# ==============================
# Printing Output using print()
# ==============================

print("\n=== Basic Print ===")

print("Hello, World!")


# ==============================
# Printing Variables
# ==============================

print("\n=== Printing Variables ===")

s = "Brad"
print(s)

s = "Anjelina"
age = 25
city = "New York"

print(s, age, city)


# ==============================
# Take Multiple Input
# ==============================

print("\n=== Multiple Input ===")

x, y = input("Enter two values: ").split()
print("Number of boys:", x)
print("Number of girls:", y)

x, y, z = input("Enter three values: ").split()
print("Total number of students:", x)
print("Number of boys is:", y)
print("Number of girls is:", z)


# ==============================
# Input as String
# ==============================

print("\n=== String Input ===")

color = input("What color is rose?: ")
print(color)


# ==============================
# Input as Integer
# ==============================

print("\n=== Integer Input ===")

n = int(input("How many roses?: "))
print(n)


# ==============================
# Input as Float
# ==============================

print("\n=== Float Input ===")

price = float(input("Price of each rose?: "))
print(price)


# ==============================
# Find Data Type
# ==============================

print("\n=== Data Types ===")

a = "Hello World"
b = 10
c = 11.22
d = ("Geeks", "for", "Geeks")
e = ["Geeks", "for", "Geeks"]
f = {"Geeks": 1, "for": 2, "Example": 3}

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))