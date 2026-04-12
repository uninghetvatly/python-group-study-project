#Format of a Python function:
#def <function_name>(<parameter1>, <parameter2>, ...):
#    <statement(s)>
#    return <value>

#Simple add function
def add(a, b):
    return a + b

print(add(5, 3))

#Iterative traversal function for a list
def traverse_list(lst):
    for item in lst:
        print(item)

traverse_list([10, 20, 30, 40])

#Recursive function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

#Leaf function
def multiply_by_two(n):
    return n * 2

#Function that calls another leaf function
def process_and_print(n):
    result = multiply_by_two(n)
    print(result)

process_and_print(10)

#Pass by Object Reference
#Python uses a mechanism known as "pass by object reference"
#The behavior depends on whether the object passed is mutable or immutable

#Immutable objects (int, float, string, tuple) behave similarly to pass-by-value
#Modifying the parameter inside the function creates a new local object
def modify_immutable(num, text):
    num = num + 10
    text = text + " World"
    print(f"Inside: num={num}, text='{text}'")

my_num = 5
my_text = "Hello"
modify_immutable(my_num, my_text)
print(f"Outside: num={my_num}, text='{my_text}'") #Originals remain unchanged

#Mutable objects (list, dict, set) behave similarly to pass-by-reference
#Modifying the object in-place alters the original object outside the function
def modify_mutable(lst, dct):
    lst.append(4)
    dct['b'] = 2
    print(f"Inside: lst={lst}, dct={dct}")

my_list = [1, 2, 3]
my_dict = {'a': 1}
modify_mutable(my_list, my_dict)
print(f"Outside: lst={my_list}, dct={my_dict}") #Originals are changed

#Reassigning a mutable object inside the function breaks the reference
#It points the local variable to a completely new object in memory
def reassign_mutable(lst):
    lst = [99, 100] #Reassignment, not in-place modification
    print(f"Inside: lst={lst}")

another_list = [1, 2, 3]
reassign_mutable(another_list)
print(f"Outside: lst={another_list}") #Original remains unchanged

