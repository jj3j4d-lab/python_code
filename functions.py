'''
Types of Python Function Arguments
Based on how the arguments are declared while defining a Python function, they are classified into the following categories −

Positional or Required Arguments

Keyword Arguments

Default Arguments

Positional-only Arguments

Keyword-only arguments

Arbitrary or Variable-length Arguments
'''

def posFun(x, y, /, z):#They are defined by placing a "/" in the function's parameter list after all positional-only parameters. 
    print(x + y + z)

print("Evaluating positional-only arguments: ")
posFun(33, 22, z=11) 

#:#Those arguments that must be specified by their name while calling the function is known as Keyword-only arguments. 
#They are defined by placing an asterisk ("*") in the function's parameter list before any keyword-only parameters. 
def posFun(*, num1, num2, num3):
    print(num1 * num2 * num3)

print("Evaluating keyword-only arguments: ")
posFun(num1=6, num2=8, num3=5) 



# Function definition is here
def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print ("Output is: ")
   print (arg1)
   for var in vartuple:
      print (var)
   return;

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50 )


##The Anonymous Functions
'''The functions are called anonymous when they are not declared in the standard manner by using the def keyword. Instead, they are defined using the lambda keyword.

Lambda forms can take any number of arguments but return just one value in the form of an expression. They cannot contain commands or multiple expressions.

An anonymous function cannot be a direct call to print because lambda requires an expression

Lambda functions have their own local namespace and cannot access variables other than those in their parameter list and those in the global namespace.

Although it appears that lambda's are a one-line version of a function, they are not equivalent to inline statements in C or C++, 
whose purpose is by passing function stack allocation during invocation for performance reasons.'''

# Function definition is here
sum = lambda arg1, arg2: arg1 + arg2;

# Now you can call sum as a function
print ("Value of total : ", sum( 10, 20 ))
print ("Value of total : ", sum( 20, 20 ))              

def my_function(a:int , b:int)->  int:
    c = a +b
    return c

print(my_function.__annotations__)


# import module_name
# from module_name import sum,average
# from mudule_name import *
# import module_name as x

'''
Module Attributes
In Python, a module is an object of module class, and hence it is characterized by attributes.

Following are the module attributes −

__file__ returns the physical name of the module.

__package__ returns the package to which the module belongs.

__doc__ returns the docstring at the top of the module if any

__dict__ returns the entire scope of the module

__name__ returns the name of the module
'''

'''
The __name__Attribute
The __name__ attribute of a Python module has great significance. Let us explore it in more detail.

In an interactive shell, __name__ attribute returns '__main__'
'''
print(__name__)

# The dir( ) Function
#The dir() built-in function returns a sorted list of strings containing the names defined by a module.

# if __name__ == "__main__":
#     print("Rahul")


def sum(*args)->int:
    total =0
    for num in args:
        total +=num
    
    return total

if __name__ == "__main__":
    s = sum(67,78,67,0,89)
    s1 = sum(54,78)

    print(s,s1,type(s),type(s1))

##*args: This is used to pack a multiple number of positional arguments into a tuple.
##**kwargs**: This is used to pack a multiple number of keyword arguments into a dictionary.

