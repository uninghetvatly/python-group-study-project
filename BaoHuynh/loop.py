#1. For loop
#FORMAT:
# # for var in iterable:
#         # statements
#         pass

#Iterable data types
# Lists: Iterates through every element in order.
#
# Tuples: Works exactly like a list, but the data cannot be changed (immutable).
#
# Strings: Iterates through every character.
#
# Dictionaries: By default, it iterates through the keys.
#
#     Use .values() for the values.
#
#     Use .items() for both key and value pairs.
#
# Sets: Iterates through unique elements in an unordered fashion.

#Using range()
# range(stop): Generates numbers from 0 to stop - 1.
for i in range(10):
    print(i)
# range(start, stop): Generates numbers from start to stop - 1.
for i in range(5, 10):
    print(i)
# range(start, stop, step): Generates numbers from start to stop - 1, incrementing by step.
for i in range (0, 10, 2):
    print(i)

#Use continue to skip specific block of codes in looping
for i in range(10):
    if i%2==0:
        continue
    else:
        print(i)

#Use break to jump out of the loop
l1=["Red","Blue","Green","Yellow","Purple"]
color=input("Enter a color:")
for i in l1:
    if i==color:
        print(i)
        break

#Use pass when the block of operation is essentially doing nothing
#Unlike continue, the rest code block still executes
for i in range(10):
    if i%2==0:
        pass
        print("This still prints after pass")
    else:
        print(i)

#Use enumerate to keep track of both the index and the item
letters = ["A", "B", "C", "D"]

for index, letters in enumerate(letters):
    print(f"{index}: {letters}")

#2. While loop
# while expression:
#     statement(s)
i=0
while i<10:
    print(i)
    i+=1