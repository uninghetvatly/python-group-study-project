# ==============================
# Loops in Python
# ==============================

# ==============================
# For Loop
# ==============================

print("=== FOR LOOP ===")

n = 4

for i in range(0, n):
    print(i)


# ==============================
# Iterating over List, Tuple, String, Dict, Set
# ==============================

print("\n=== Iterate over collections ===")

li = ["geeks", "for", "geeks"]
for x in li:
    print(x)

tup = ("geeks", "for", "geeks")
for x in tup:
    print(x)

s = "abc"
for x in s:
    print(x)

d = {'x': 123, 'y': 354}
for x in d:
    print("%s  %d" % (x, d[x]))

set1 = {10, 30, 20}
for x in set1:
    print(x)


# ==============================
# Iterating by Index
# ==============================

print("\n=== Iterate by index ===")

li = ["geeks", "for", "geeks"]

for index in range(len(li)):
    print(li[index])


# ==============================
# While Loop
# ==============================

print("\n=== WHILE LOOP ===")

cnt = 0

while cnt < 3:
    cnt = cnt + 1
    print("Hello Geek")


# ==============================
# Infinite While Loop (Safe Demo)
# ==============================

print("\n=== Infinite Loop Demo (with break) ===")

count = 0

while True:
    print("Hello Geek")
    count += 1
    if count == 3:   # tránh chạy vô hạn
        break


# ==============================
# Nested Loops
# ==============================

print("\n=== Nested Loops ===")

for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()


# ==============================
# Continue Statement
# ==============================

print("\n=== Continue Statement ===")

for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        continue
    print('Current Letter :', letter)


# ==============================
# Break Statement
# ==============================

print("\n=== Break Statement ===")

for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        break

print('Current Letter :', letter)


# ==============================
# Pass Statement
# ==============================

print("\n=== Pass Statement ===")

for letter in 'geeksforgeeks':
    pass

print('Last Letter :', letter)