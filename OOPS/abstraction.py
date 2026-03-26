'''Abstraction is one of the important principles of object-oriented programming. It refers to a programming approach by which only 
the relevant data about an object is exposed, hiding all the other details. 
This approach helps in reducing the complexity and increasing the efficiency of application development.
1. Data Abstraction
2. Process Abstraction
'''

#Python Abstract Class
'''Key Points
ABC → makes class abstract
@abstractmethod → method must be implemented in child class
You cannot create object of abstract class
abstractmethos Must override in child'''

from abc import ABC, abstractmethod
class Vehicle(ABC):   # 👈 inherit from ABC

    @abstractmethod
    def start(self):
        print("In abstract class")
        pass

class Car(Vehicle):

    def start(self):
        super().start()
        print("Car starts with key")

c = Car()
c.start()

################### Encapsulation ###########################
'''Encapsulation is the process of bundling attributes and methods within a single unit.
It is one of the main pillars on which the object-oriented programming paradigm is based.
In this The actual access modifiers come into picture'''

# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# s1 = Student("rahul",24)
# print(s1.name,s1.age)

'''In the above example, the instance variables are initialized inside the class. 
However, there is no restriction on accessing the value of instance variables from outside the class, which is against the principle of encapsulation.'''

class Student:

   def __init__(self, name="Rajaram", marks=50):
      self.__name = name
      self.__marks = marks
   def studentdata(self):
      print ("Name: {} marks: {}".format(self.__name, self.__marks))
      
s1 = Student()
s2 = Student("Bharat", 25)

s1.studentdata()
s2.studentdata()
print ("Name: {} marks: {}".format(s1._Student__name, s1._Student__marks))
# print ("Name: {} marks: {}".format(s2.name, s2.marks))

'''
What is Name Mangling?
Python doesn't block access to private data entirely. It just leaves it to the wisdom of the programmer, 
not to write any code that accesses it from outside the class. You can still access the private members by Python's name mangling technique.

Name mangling is the process of changing name of a member with double underscore to the form object._class__variable. 
If so required, it can still be accessed from outside the class, but the practice should be refrained.'''