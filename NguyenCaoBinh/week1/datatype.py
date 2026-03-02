# ==============================
# Python Data Types
# ==============================

print("=== Assign Different Data Types ===")

x = 50          # int
x = 60.5        # float
x = "Hello World"   # string
x = ["geeks", "for", "geeks"]   # list
x = ("geeks", "for", "geeks")   # tuple

print(x)


# ==============================
# 1. Numeric Data Types
# ==============================

print("\n=== Numeric Data Types ===")

a = 5
print(type(a))

b = 5.0
print(type(b))

c = 2 + 4j
print(type(c))


# ==============================
# 2. Sequence Data Types - String
# ==============================

print("\n=== String Data Type ===")

s = 'Welcome to the Geeks World'
print(s)

print(type(s))

print(s[1])
print(s[2])
print(s[-1])


# ==============================
# List Data Type
# ==============================

print("\n=== List Data Type ===")

# Empty list
a = []

# list with int values
a = [1, 2, 3]
print(a)

# mixed list
b = ["Geeks", "For", "Geeks", 4, 5]
print(b)

print("Accessing element from list")
print(b[0])
print(b[2])

print("Accessing using negative indexing")
print(b[-1])
print(b[-3])


# ==============================
# Tuple Data Type
# ==============================

print("\n=== Tuple Data Type ===")

tup1 = ()
tup2 = ('Geeks', 'For')

print("Tuple:", tup2)

tup1 = (1, 2, 3, 4, 5)

print(tup1[0])
print(tup1[-1])
print(tup1[-3])


# ==============================
# 3. Boolean Data Type
# ==============================

print("\n=== Boolean Data Type ===")

print(type(True))
print(type(False))

# Truthy / Falsy
if 1:
    print("1 is truthy")

if not 0:
    print("0 is falsy")


# ==============================
# 4. Set Data Type
# ==============================

print("\n=== Set Data Type ===")

s1 = set()

s1 = set("GeeksForGeeks")
print("Set from string:", s1)

s2 = set(["Geeks", "For", "Geeks"])
print("Set from list:", s2)

set1 = set(["Geeks", "For", "Geeks"])
print(set1)

print("Loop through set:")
for i in set1:
    print(i, end=" ")

print("\nCheck item exist:")
print("Geeks" in set1)


# ==============================
# 5. Dictionary Data Type
# ==============================

print("\n=== Dictionary Data Type ===")

d = {}
d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(d)

d1 = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
print(d1)

d = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}

print(d['name'])
print(d.get(3))