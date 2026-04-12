#1. Input operations
#input() function takes user input and returns in string form by default
name=input("Your name is: ")
print(name,"is your name")

obj=input("Enter your age: ")
print(type(obj)) #type str, not int

#Taking in multiple inputs using .split()
#User inputs a single line separating items using whitespace, tabs, new lines,...
a,b=input("Enter two natural numbers: ").split()
print(a)
print(b)

# Input a List
list1 = input("Enter items separated by space: ").split()
# Result: [<item1>, <item2>,...]

# Input a Tuple
tuple1 = tuple(input("Enter x and y (e.g. 10,20): ").split(","))
# Result: (<item1>, <item2>)

# Input a Dictionary
user_data = {}
pair = input("Enter key and value separated by colon: ")
key, value = pair.split(":")
user_data[key] = value

#2. Output operations
#When printing multiple variables and string, each must be separated by comma
s1="Huynh"
s2="Gia"
s3="Bao"
print(s1,s2,s3)

