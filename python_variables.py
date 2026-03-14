'''Python variables do not need explicit declaration to reserve memory space or you can say to create a variable. 
A Python variable is created automatically when you assign a value to it. 
The equal sign (=) is used to assign values to variables.'''


counter = 10
counter1 = 100.01
name = "Rahul"

print("counter:{} counter1:{} name:{}".format(counter, counter1, name))#printing using format function
print(f"counter:{counter} counter1:{counter1} name:{name}") #printing using f string most commonly used
print("counter:%d counter1:%.2f name:%s" % (counter, counter1, name)) # printint using old style


# Deleting a Python variable  del var_a, var_b
'''del counter
print(counter)#it will throw an error'''

#Getting Type of a Variable
print(f"Type of counter:{type(counter)} counter1;{type(counter1)} name{type(name)}")


#Casting Python Variables
#You can specify the data type of a variable with the help of casting as follows:

x = int(10) # it will make x as integer type and assign 10 int it
s = str(10) # it will assign s as string type and assign 10 as string to s
f = float(10) #it will assign f as float type and assign 10.0 to it
print(f"Type of x:{type(x)} s:{type(s)} f:{type(f)}")


#Python Variables - Multiple Assignment
# a=b=c = 10 #correct
a,b,c = 10,20,30 #correct
print(a,b,c)

'''Camel case − First letter is a lowercase, but first letter of each subsequent word is in uppercase. For example: kmPerHour, pricePerLitre

Pascal case − First letter of each word is in uppercase. For example: KmPerHour, PricePerLitre

Snake case − Use single underscore (_) character to separate words. For example: km_per_hour, price_per_litre'''

#Constants in Python
'''Python doesn't have any formally defined constants, However you can indicate a variable to be treated as a constant by using 
all-caps names with underscores. 
For example, the name PI_VALUE indicates that you don't want the variable redefined or changed in any way.'''

#Defining Private Variables in Python
'''In Python, private variables are defined by adding a double underscore (__) before the variable name. '''
'''
Feature	              Public Variables	                                 Protected Variables	                                                Private Variables
Definition	         Variables that can be accessed from anywhere.	     Variables that can be accessed within the class and its subclasses.	Variables that can only be accessed within the class they are defined in.
Syntax	             int var	                                         int _var	                                                            int __var
Security	         Least secure	                                      Moderately secure	                                                    Most secure
Example	             int age = 25	                                      int _age = 25	                                                        int __age = 25
'''