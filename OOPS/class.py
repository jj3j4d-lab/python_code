'''What is a Class in Python?
In Python, a class is a user defined entity (data types) that defines the type of data an object can contain and the actions it can perform.
 It is used as a template for creating objects. '''

class Employee:
    emp_count = 0

    def __init__(self,name,salary): # self is the object iteself.like emp1 is self for instance emp1
        self.name = name
        self.salary = salary
        Employee.emp_count += 1

    def print_emp(self):
        print(f"Employee name:{self.name} Employee Salary:{self.salary}")
    
    def print_count(self):
        print(f"Employee Count is:{Employee.emp_count}") # emp_count is class variable so accessing it using Emploee.em_count

# if __name__ == "__main__":
#     emp1 = Employee("ZARA",2000)
#     emp2 = Employee("Rahul",3000)
#     emp2.print_count()
#     emp1.print_count()

# There are two types of attribute 1. Class attribute like emp_count above 2. instance attribute like name and salary above
# There are three types of methods 
'''
1. Class methods:A Python class method is a method that is bound to the class and not to the instance of the class. 
It can be called on the class itself, rather than on an instance of the class.
Creating Class Methods in Python
There are two ways to create class methods in Python −

Using classmethod() Function
Using @classmethod Decorator'''

class Employee:
    empCount = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Employee.empCount += 1

    @classmethod
    def showcount(cls):
        print (cls.empCount)

    @classmethod
    def newemployee(cls, name, age):
        return cls(name, age)

e1 = Employee("Bhavana", 24)
e2 = Employee("Rajesh", 26)
e3 = Employee("John", 27)
e4 = Employee.newemployee("Anil", 21)

Employee.showcount()
    


