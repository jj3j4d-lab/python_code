# Slicing a string
str1 = "Rahul"
print(str1[2:4])

print(str1[2:5]) #  positive indexing
print(str1[-5:-1])# negative indexing

'''Converting a string into list
'''
l1 = list(str1)
print(str1,l1)

'''Concat of string'''
str2 = "jj"
print(str1 + str2)

'''Print number into different systems'''
num = 25

print(f"Decimal: {num}")
print(f"Binary : {num:b}")
print(f"Octal  : {num:o}")
print(f"Hex    : {num:x}")
print(f"HEX :{num:X}")


'''There are almost every built in fucntion exist for string operation so you can use it'''