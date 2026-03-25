# Importing array in python
import array as arr
import copy

#creating an array with differnt types
arr1 = arr.array('i',[1,2,34,5,6]) # integer type array
arr2 = arr.array('u', 'BAT') # character type array
arr3  = arr.array('d',[1.1,1.3,1.4])

print(type(arr1),arr1)
print(type(arr2),arr2)
print(type(arr3),arr3)

# Array Elements Accessing
# 1. using enemurate() function

for loc , val in enumerate(arr1):
    print(f"Index:{loc} j has element:{val}")

# 2. using Iteration
for i in arr3:
    print(i)

###############  Adding an element in array ###############
#1. using append function
arr1.append(3)
print(arr1)

# 2. using insert method
arr3.insert(2,2.2)
print(arr3)

# Using extend method
arr4 = arr.array('d',[1.6,3.7,4.8,8.9])
arr3.extend(arr4)
print(arr3)

################Removing Elements from array ####################
#1. using remove function
arr4.remove(3.7)
print(arr4)

# 2. Using ,pop()
arr4.pop(1)
print(arr4)

#################### Copy an array to another #############

a = arr1
print(a)

# use of deep copy(it make another physical copy)
b = copy.deepcopy(a)
print(b,memoryview(b),memoryview(a),memoryview(arr1))
c = arr.array('i')

################ Reversing an array ###############
# 1. Using reverse() -> Issue is you have to convert array to list , then reverse it using reverse() Then convert back reversed list to array
# 2. reversed() -> it accepts array ar argument
# 3. using Slicing operation : (:: -1)
# 4. using for loop
for i in range(len(arr1)-1,-1,-1):
    c.append(arr1[i])
print(c)


################# Sorting of array ################
#1. using sort() but same it is for list
# 2. using sorted functiomn as it accept array as argument
# 3. using sorting algorithm

arrrr = []
for i in range(5):
    arrrr.insert(i,i+1)
print(arrrr)
