################ Python Packages #############E
# Creating a Python Package 
import os

# new_dir = 'Python_package'
# os.makedirs(new_dir)

# new_dir = '/home/rahul/Documents/coding/Python/OOPS/Python_package/my_python_package'
# os.makedirs(new_dir)

''' Python Packages are elaborated in python_packages '''

############### Inner Class ############
'''A class defined inside another class is known as an inner class in Python. Sometimes inner class is also called nested class.
If the inner class is instantiated, the object of inner class can also be used by the parent class. 
Object of inner class becomes one of the attributes of the outer class. 
Inner class automatically inherits the attributes of the outer class without formally establishing inheritance.
1. Multiple Inner Class
In multiple inner class, a single outer class contains more than one inner class. 
Each inner class works independently but it can interact with the members of outer class.

2. Multilevel Inner Class
It refers to an inner class that itself contains another inner class. It creates multiple levels of nested classes.
'''

#Example of Inner class
class Outer:
    def __init__(self):
        self.name = 'Ashish'
        self.subs = self.Inner()
        return
    def show(self):
        print(f"Name : {self.name}")
        self.subs.display()
    
    class Inner:
        def __init__(self):
            self.sub1 = 'Phy'
            self.sub2 = 'Chem'    
            return
        def display(self):
            print(f"sub1:{self.sub1} sub2: {self.sub2}")
s1 = Outer()
s1.show()


################ Anonymous class ##################


################### Singleton Class ###############
'''In Python, a Singleton class is the implementation of singleton design pattern which means this type of class can have only one object. 
This helps in optimizing memory usage when you perform some heavy operation, like creating a database connection.
If we try to create multiple objects for a singleton class, the object will be created only for the first time. After that, the same object instance will be returned
####### Creating a Singleton class
1. Using __init__ method
2. using new() method :: When an instance of a Python class is declared, it internally calls the __new__() method. 
If you want to implement a Singleton class, you can override this method.
'''
# 1. Using __init__ method()
class Singleton:
    __uniqueInstance = None
    
    @staticmethod
    def createInstance():
        if Singleton.__uniqueInstance == None :
            Singleton()
        return Singleton.__uniqueInstance
    def __init__(self):
        if Singleton.__uniqueInstance != None:
            raise("Object Already Exist")
        else:
            Singleton.__uniqueInstance = self

s = Singleton.createInstance()
s2 = Singleton.createInstance()
print(s,s2)


# 2. using new() Method
class SingletonClass:
   _instance = None
   
   def __new__(cls):
      if cls._instance is None:
         print('Creating the object')
         cls._instance = super(SingletonClass, cls).__new__(cls)
      return cls._instance
      
obj1 = SingletonClass()
print(obj1)

obj2 = SingletonClass()
print(obj2)

###################### Wrapper Class ################

############### Enums in Python ################
'''
In Python, the term enumeration refers to the process of assigning fixed constant values to a set of strings so that each string can be identified by the value bound to it. 
The Enum class included in enum module (which is a part of Python's standard library) is used as the parent class to define enumeration of a set of identifiers −
conventionally written in upper case.
An enum class cannot have the same member appearing twice, 
however, more than one member may be assigned the same value. To ensure that each member has a unique value bound to it, use the @unique decorator.'''
# importing enum 
from enum import Enum

class subjects(Enum):
   ENGLISH = 1
   MATHS = 2
   SCIENCE = 3
   SANSKRIT = 4

obj = subjects.MATHS
print (type(obj))

subject = Enum("subjects", "ENGLISH MATHS SCIENCE SANSKRIT")
print(subject.ENGLISH)
print(subject.MATHS)
print(subject.SCIENCE)
print(subject.SANSKRIT)

# Accessing Modes in Enums
print(obj.name)
print(obj.value)

# Iterating through enums
for sub in subjects:
    print(sub.name,sub.value)
    
################ Python Reflection #############
'''In object-oriented programming, reflection refers to the ability to extract information about any object in use. 
You can get to know the type of object, whether is it a subclass of any other class, what are its attributes, and much more. 
Python's standard library has several functions that reflect on different properties of an object. Reflection is also sometimes called introspect.

Following is the list of reflection functions in Python −

type() Function
isinstance() Function
issubclass() Function
callable() Function
getattr() Function
setattr() Function
hasattr() Function
dir() Function'''

from dataclasses import dataclass  

@dataclass  
class Student:  
    name: str  
    age: int  
    percent: float

s3 = Student("Alice", 20, 90.0)
s4 = Student("Bob", 22, 85.5)

print(s3)         
print(s4 == s3) 