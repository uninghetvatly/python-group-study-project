#1. if-else conditional statement
#FORMAT:
# if condition:
# \tab    # Code to run if true
# elif another_condition:
# \tab  # Code to run if the first is false
# else:
# \tab  # Code to run if all above are false

a=int(input("Enter a number: "))
if a < 0:
    print(a,"is negative")
else:
    print(a,"is positive")

#Adding logical operator

if a>=0 and a<=10:
    print(a, "is a valid score")

if 0<=a<=10: #this is the same as the above
    print(a, "is an invalid score")

#Nested conditional statement
#tab the whole block of if-else statement to make it nested

if 0<=a<=10:
    if 5<=a<=10:
        print(a, "is an above average score")
    else:
        print(a, "is a below average score")
else:
    print(a, "is an invalid score")

#2. Ternary conditional statement
#FORMAT: var = true_operation if (<condition>) else false_operation
res="Negative" if a<0 else "Positive"
print(res)

#3. Match case statement
#FORMAT:
# match subject:
#     case pattern1:
#         # Code block if pattern1 matches
#     case pattern2:
#         # Code block if pattern2 matches
#     case _:
#         # Default case (wildcard) if no other pattern matches

#Data type:
# Integers: case 1:
# Strings: case "admin":
# Booleans: case True:
# None: case None:
# Floats: case 3.14:


#Use logical | operator for matching or

prime=int(input("Enter a number: "))
if 0<=prime<10:
    match prime:
        case 2 | 3 | 5 | 7:
            print(prime, "is a one-digit prime number")
        case _:
            print(prime, "is not a one-digit prime number")
else:
    print(prime, "is not one digit")

#Combining if statement within match case

name=input("Enter your name: ")
age=int(input("Enter your age: "))
match name:
    case "Bao" if age==18:
        print("Hello me")
    case "Bao" if age>18:
        print("Hello older me")
    case "Bao" if age<18:
        print("Hello younger me")
    case _:
        print("Hello")

#match structure
#List: case [x, y]:
data=input("Enter items separated by space: ").split()
match data:
    case [x, y]:
        # A list with two elements
        print(f"Two-element list: {x}, {y}")
    case [x, y, z]:
        # A list with three elements
        print(f"Three-element list: {x}, {y}, {z}")
    case _:
        print("Unknown data format")

#Tuple: case (x,y):
data = tuple(input("Enter items in tuple: ").split(","))
match data:
    case (x, y):
        # A tuple with two elements
        print(f"Two-element tuple: {x}, {y}")
    case (x, y, z):
        # A tuple with three elements
        print(f"Three-element tuple: {x}, {y}, {z}")
    case _:
        print("Unknown data format")
#Dictionary: case {"role": "admin", "id": id}:
user_data = {}
pair = input("Enter name and age or only name separated by colon: ")
key, value = pair.split(":")
user_data[key] = value
match user_data:
    # Dictionary with name and age keys
    case {"name": name, "age": age}:
        print(f"Name: {name}, Age: {age}")

    # Dictionary with only name key
    case {"name": name}:
        print(f"Name: {name}")
    case _:
        print("Unknown format")

