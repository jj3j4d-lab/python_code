# if statment

if 3>5:
    print("If is true")
elif 5>3:
    print("elif is true")
else:
    print("esle is true")


# match-case statement 
'''With the release of Python 3.10, a pattern matching technique called match-case has been introduced, 
which is similar to the switch-case construct available in C/C++/Java etc. '''

def weekday(n):
   match n:
      case 0: return "Monday"
      case 1: return "Tuesday"
      case 2: return "Wednesday"
      case 3: return "Thursday"
      case 4: return "Friday"
      case 5: return "Saturday"
      case 6: return "Sunday"
      case _: return "Invalid day number"
print (weekday(3))
print (weekday(6))
print (weekday(7))

#case combinned statement
def access(user):
    match user:
        case "admin" | "manager": 
            return "Full access"
        case "client" | "Developer":
            return "Limited access"
        case _:
            return "No access"

print(access("admin"))
print(access("Developer"))
print(access("agsfgsd"))

# you can pass list of argumnets in cases
# you can use if statement in cases
#like case [amt,dur] if amt<1000
            #return amt*dur


# loops in python
# 1. For 2. while 3. nested loops

''' for loop with else'''
for i in range(5):
    print(i)
else:
    print("out of for loo")

while i<7:
    i +=1
    print(i)

'''Python control statement'''
#1. break :Python break statement is used to terminate the current loop and resumes execution at the next statement, just like the traditional break statement in C.
#2. continue: Python continue statement is used to skip the execution of the program block and returns the control to the beginning of the current loop to start the next iteration.
#3. pass : Python pass statement is used when a statement is required syntactically but you do not want any command or code to execute.
#4. return