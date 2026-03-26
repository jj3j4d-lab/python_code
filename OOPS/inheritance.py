'''Inheritance is one of the most important features of object-oriented programming languages like Python. 
It is used to inherit the properties and behaviours of one class to another. 
The class that inherits another class is called a child class and the class that gets inherited is called a base class or parent class.
Types of Inheritance
In Python, inheritance can be divided in five different categories −
Single Inheritance
Multiple Inheritance
Multilevel Inheritance
Hierarchical Inheritance
Hybrid Inheritance
'''

# Single Inheritance
class Vehicle:
    def v1(self):
        print("I am Vehicle")
    
class car(Vehicle):
    def c1(self):
        print("I am car class")



# if __name__ == "__main__":
#     c = car()
#     c.c1()
#     c.v1()

# Multiple Inheritance: Multiple inheritance in Python allows you to construct a class based on more than one parent classes. 
'''class parent1:
   #statements
   
class parent2:
   #statements
   
class child(parent1, parent2):
   #statements'''
#Each Python has a mro() method that returns the hierarchical order that Python uses to resolve the method to be called.
#  The resolution order is from bottom of inheritance order to top.

# Multilevel Inheritance :  In multilevel inheritance, a class is derived from another derived class. There exists multiple layers of inheritance. 
# We can imagine it as a grandparent-parent-child relationship.

# parent class
class Universe: 
   def universeMethod(self):
      print ("I am in the Universe")

# child class
class Earth(Universe): 
   def earthMethod(self):
      print ("I am on Earth")
      
# another child class
class India(Earth): 
   def indianMethod(self):
      print ("I am in India")      

# creating instance 
person = India()  
# method calls
person.universeMethod() 
person.earthMethod() 
person.indianMethod() 

# Hirarchical Inheritance
#this type of inheritance contains multiple derived classes that are inherited from a single base class. 

# Hybrid Inheritance : Combination of two or more types of inheritance is called as Hybrid Inheritance. 
# For instance, it could be a mix of single and multiple inheritance.

''' The super() method : In Python, super() function allows you to access methods and attributes of the parent class from within a child class.'''
class Parent:
   counter = 0
   def __init__(self,a,b):
      self.a = a
      self.b = b
    
   def counterIn(self):
      for i in range(5):
         Parent.counter +=1
   
class child(Parent):
   def __init__(self):
      print(super().counter)
       
      
c2 = child()
c2.counterIn()
c2 = child()
print(child.mro())

'''Diamond Problem in Multiple Inheritance
The diamond problem is a common issue in multiple inheritance. 
It arises when two parent classes inherit from the same base class, and a child class inherits from both parent classes.'''