from multipledispatch import dispatch
'''What is Polymorphism in Python?
The term polymorphism refers to a function or method taking different forms in different contexts. 
Since Python is a dynamically typed language, polymorphism in Python is very easily implemented.

If a method in a parent class is overridden with different business logic in its different child classes, the base class method is a polymorphic method.
There are four ways to implement polymorphism in Python −

Duck Typing
Operator Overloading
Method Overriding
Method Overloading
'''

# Duck Typing: Duck typing is a concept where the type or class of an object is less important than the methods it defines.
# Using this concept, you can call any method on an object without checking its type, as long as the method exists.

# Method Overriding
'''In method overriding, a method defined inside a subclass has the same name as a method in its superclass but implements a different functionality.'''
class Employee:
   def __init__(self,nm, sal):
      self.name=nm
      self.salary=sal
   def getName(self):
      return self.name
   def getSalary(self):
      return self.salary

class SalesOfficer(Employee):
   def __init__(self,nm, sal, inc):
      super().__init__(nm,sal)
      self.incnt=inc
   def getSalary(self):
      return self.salary+self.incnt

e1=Employee("Rajesh", 9000)
print ("Total salary for {} is Rs {}".format(e1.getName(),e1.getSalary()))
s1=SalesOfficer('Kiran', 10000, 1000)
print ("Total salary for {} is Rs {}".format(s1.getName(),s1.getSalary()))

#################### Method Overloading ##############
'''Method overloading is a feature of object-oriented programming where a class can have multiple methods with the same name but different parameters.'''
# from multipledispatch import dispatch
class example:
   @dispatch(int, int)
   def add(self, a, b):
      x = a+b
      return x
   @dispatch(int, int, int)
   def add(self, a, b, c):
      x = a+b+c
      return x

obj = example()

print (obj.add(10,20,30))
print (obj.add(10,20))

'''In object-oriented programming, the concept of dynamic binding is closely related to polymorphism. 
In Python, dynamic binding is the process of resolving a method or attribute at runtime, instead of at compile time.'''
class shape:
   def draw(self):
      print ("draw method")
      return

class circle(shape):
   def draw(self):
      print ("Draw a circle")
      return

class rectangle(shape):
   def draw(self):
      print ("Draw a rectangle")
      return

shapes = [circle(), rectangle()]
for shp in shapes:
   shp.draw()