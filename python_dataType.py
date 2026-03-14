#Types of Datatype in python
'''Numeric Data Types
      int
      float
     complex
String Data Types
Sequence Data Types
     list
     tuple
     range
Binary Data Types
     bytes
     bytearray
memoryview
Dictionary Data Type
Set Data Type
     set
     frozenset
Boolean Data Type
None Type'''

############################# sequence data type ###################
 # 1. List
l = ['a',2,'Rahu',4.0]
l1 = ['b',3,'jj']
print(l,type(l))
#Access of Elements in list using Slice operator
print(f"Element at 0:{l[0]} Element from 0 to 3:{[l[0:3]]}")
print(f"Printing list twice:{l * 2}")
print(f"Concating the list:{l + l1}")


# 2. Tuple 
t = ('q',2,'jj')
print(f"Printing tuple with type:{t}{type(t)}")

# list and tuple both are accessed using the slice operator:

'''The main differences between lists and tuples are: Lists are enclosed in brackets ( [ ] ) and 
their elements and size can be changed i.e. lists are mutable, while tuples are enclosed in parentheses ( ( ) )
 and cannot be updated (immutable). Tuples can be thought of as read-only lists.
 A Python range is an immutable sequence of numbers which is typically used to iterate through a specific number of items.'''

 # 3. range
 # range(start,stop,step)  we cannnot give 0 as argumnet for step in rannge
for i in range(1,11,2):
    print(i)


################ Binary DataTypes ####################
#1. bytes
b = bytes([61,62,63,64,65])
print(b,type(b))

#2. Bytearray 
b1 = bytearray([72, 101, 108, 108, 111]) # bytearrya is mutable while bytes is not
print(b1,type(b1))

#3. memoryview
b2 = bytearray([1,21,4,67])
print(memoryview(b2))

############ Dictionary Datatype #############
d = {'name':'Rahul','Age':24,'Work':'BEL',1:'one'} # Dictionary is mutable
print(d,type(d))
print(f"Printing only keys of d:{d.keys()}")
print(f"printing only values of d:{d.values()}")

print("Printing keys using for loop")
for key in d.keys():
    print(key)

print("Printing only values of d")
for value in d.values():
    print(value)

print("printing keys and values")
for i in d.items():
    print(i)

################### Set Data Type ##################
''' An object cannot appear more than once in a set, whereas in List and Tuple, same object can appear more than once.
Hashing is a mechanism in computer science which enables quicker searching of objects in computer's memory. Only immutable objects are hashable.'''
set1 = {4,6,2,9,0}
set2 = {0,2,4,6,10}
print(set1)
print(set2)

################# Boolean Data type #####################
x = True
y = False
print(type(x),type(y))

################ None Data Type
"""Python's none type is represented by the "nonetype." It is an object of its own data type.
 The nonetype represents the null type of values or absence of a value.
"""
z = None
print(z,type(z))