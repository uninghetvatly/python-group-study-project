#1.Numeric data types
#Check for data types using print(type(var))
a=5
print(type(a))
a=5.4
print(type(a))
a=3+8.5j
print(type(a))

#2. Dictionary
#Similar to arrays but with indexing using keys
#Format: <key>:<item>.
#Key can only be string, numeric, booleans and tuples.
#Keys and items can be of different data types within a dictionary
#Item can be of any data types
d1={1:'a', 'b':2, 3+4j:"abcd"}

#dict constructor: dict([(key1=item1), (key2=item2)...])
d2 = dict([(1,"Huynh"), (2,"Gia"), (3,"Bao")])

#Use print(<dictionary name>) to print the whole thing
print(d1)
print(d2)

#Use print(<dictionary name>[<index>])  or .get(<index>) to access an element
print(d1[3+4j])
print(d2.get(3))

#.item() retrieves a view object containing a list of tuples. Each tuple represents a key-value pair from the dictionary.
print(list(d1.items())[1][0]) #print key of item with index 1
print(list(d1.items())[1][1]) #print val of item with index 1

#Adding (to the tail) and updating using index access
d1["newKey"]="dcba"
print(d1)

#d1.update(d2): Compare key value of d2 to d1 and update d1 val to d2 val if equal
dict1 = {'Name': 'Bao', 'Age': '20', 'Nationality': 'Vietnam'}
dict2 = {'Name': 'Khang', 'Age': '22'}

dict1.update(dict2)
print(dict1)
print(d1)
#Removing an item using del, .pop(index), .clear() (clear the whole thing), .popitem() (to pop the last)
del d1[1]
print(d1)
val=d1.pop('b')
print(d1)
print(val)
key, val=d1.popitem()
print(key)
print(val)
d1.clear()
print(d1)

#.keys() returns a view object with dictionary keys
print(list(d1.keys()))

#.values() returns a view object containing all dictionary values
print(list(d1.values()))

#Iterate using for loop
#Iterate through keys
for key in d2:
    print(key)

#Iterate through items
for item in d2:
    print(item)

#Iterate through pairs
for key, item in d2.items():
    print(f"{key}:{item}")

#Nested dictionary
library={"Comics": {1:"DC", 2:"Marvel"}, "Novel":{1:"Sherlock", 2:"Kidnap tour"}}
print(library)
print(library["Comics"][2])

#3. Booleans
#Anything empty, None, 0, 0.0 is false when using bool()
x = None
print(bool(x))
x = ()
print(bool(x))
x = {}
print(bool(x))
x = 0.0
print(bool(x))

#4 Sets
#No duplicate items, but items can be of different data types: numeric, string, typle, bool
s1={1,2,1,3,4,5,6,7, 'a','b','c','d'} #only prints 1,2,3,4,5,6,7, a, b, c, d
print(s1)
#Can not access using index and can not change item in the set directly
#Type cast from list, tuples to sets
s2=set([1,3,5,7])
print(s2)

#Can add and remove item using .add(item) and .remove(item)
s1.add(3+4j)
print(s1)
s1.remove(3+4j)
print(s1)

#frozenset() can not be changed, removed, or added, but can use union, intersection and difference
fs1 = frozenset(["e", "f", "g",1,2,3])
fs2 = frozenset(["e", "b", "g",1,4,3])
#s1.difference(s2) (in s1 but not s2), union(), intersection()
fs=fs1.intersection(fs2)
print(fs)
fs=fs1.union(fs2)
print(fs)
fs=fs1.difference(fs2)
print(fs)

#Operators
#checking in or not in
a=1 in s1
print(a)
b="g" not in fs1
print(b)
#Use <=, < to check for subset and proper subset, similar for other operators
print(s1>s2)
#Use | for union, & for intersection. - for difference and ^ for xor
fs=fs1^fs2
print(fs)

#5. String
#String can be constructed using '', ""
st1="Huynh Gia Bao"
st2='Huynh Gia Bao'
print(st1==st2)

#Multi line using '''   '''
st='''Huynh
Gia 
Bao
'''
print(st)

#Indexes of string are of two types: pos and neg
# String:       H   u   y   n   h   _   G   i   a   _   B   a   o
# Positive:     0   1   2   3   4   5   6   7   8   9  10  11  12
# Negative:   -13 -12 -11 -10  -9  -8  -7  -6  -5  -4  -3  -2  -1

#Substring using st[start:end] (excluding end, meaning end-1 only)
#Not specifying end means til the end of the string
print(st1[3:8])
print(st1[3:])
#Iterate through string
for char in st1:
    print(char)

#Can not change string value after created. But can use concatenation, slice and format
#Incorrect: st1[1]='G'
st3=st1[0:10]+ "Khang"
print(st3)

#Delete a string, can not access deleted string
del st2

#Update a string using .replace(<replaced substring>, <added substring>)
st1=st1.replace("Khang", "Bao")
print(st1)

#Length of string using len(s)
print(len(st1))

#Change case using upper() and lower()
print(st1.upper())
print(st1.lower())

#Remove unnecessary white spaces using .strip()
st="    Huynh   Gia    "
st=st.strip()
print(st)

#Combine string using + operator
stFirst="Huynh Gia "
stLast="Bao"
stFull=stFirst+stLast
print(stFull)

#Repeat string using * operator
stLast=stLast*4
print(stLast)

#Format string using f-strings to embed var and expressions using {}
print(f"My name is {st1}")

#Format string using .format()
print("my name is {} and I am {}".format(st1, 18))

#Check if a substring exists using keyword in
print("Bao" in st1)

#6. List
#Can be of mixed data types
#Created using []
l1=[1,2,3,'a','b','c']
print(l1)
#List constructor
l2=list((1.1,1.2,1.3))
print(l2)
l2=list("Huynh Gia Bao") #each char is an item
print(l2)
#Creating with repeated items
l2=[2,3]*5  #2,3 5 times
print(l2)
#Indexes can be in positive order or negative order

#Adding an item at the end using .append(<item>)
l1.append('d')
print(l1)

#Adding a list (or multiple items) at the end using .extend(<list>)
l1.extend(['e','f'])
l1.extend(l2)
print(l1)

#Add an item at an index using .insert(<index>, <item>)
l2.insert(2,'r')
print(l2)

#Clear a list
l2.clear()
print(l2)

#Mutable, can update item after created
l1[0]='H'
print(l1)

#Remove first occurrence of an item using .remove(<item>)
l1.remove('H')
print(l1)

#Remove at index using .pop(<index>) or could use del list[<index>]
#If no index is specified, remove the last one
l1.pop(1)
print(l1)
del(l1[1])
print(l1)

#Iterate through list
for it in l1:
    print(it)

#Nested list
matrix = [ [1, 2, 3],
           [4, 5, 6],
           [7, 8, 9] ]
print(matrix[1][2])

#Shallow copy using .copy()
copyList=l1.copy()
print(copyList)

#Count num of occurrences of an item in the list using .count(<item>)
print(l1.count(2))

#Return the index of the first item with that val using .index()
print(l1.index(2))

#.reverse()
l1.reverse()
print(l1)

#sort list using .sort(). Only applied to single data type int, or char
lSort=[]
for item in l1:
    if type(item)==int:
        lSort+=[item]
lSort.sort()
print(lSort)


#7. Tuple
#Similar to list with objects separated by ',', indexing, nested and repetition
#Immutable, can not change items
t1=(1,2,3,'a','b','c')
print(t1)

#Can access elements using index (pos and neg)
#Can not append, extend, remove, update
print(t1[0])

#Iterate similar to list
for item in t1:
    print(item)

#Concatenation using operator +
t2=('d','e','f',4,6,8)
t=t1+t2
print(t)

