#Types of python Operators
"""Arithmetic Operators
Comparison (Relational) Operators
Assignment Operators
Logical Operators
Bitwise Operators
Membership Operators
Identity Operators"""

# 1. Arithmatic operators
'''Addition(+),Substraction(-),Multiplication(*)
Division(/), Modulo(%),Exponent(**),floor division(//)'''

print(9//4)

# 2. Comaprison Operators
"""==	Equal	
!=	Not equal
>	Greater than	
<	Less than	
>=	Greater than or equal to	
<=	Less than or equal to	"""

# 3. Assignment operators
'''Operator	Example	       Same As
=	         a = 10	        a = 10
+=	         a += 30	    a = a + 30
-=	         a -= 15	    a = a - 15
*=	         a *= 10	    a = a * 10
/=	         a /= 5	        a = a / 5
%=	         a %= 5	        a = a % 5
**=	         a **= 4	    a = a ** 4
//=	         a //= 5	    a = a // 5
&=	         a &= 5	        a = a & 5 
|=	         a |= 5	        a = a | 5 bit wise or 
^=	         a ^= 5	        a = a ^ 5bitwise and
>>=	         a >>= 5	    a = a >> 5 # Right shift  shortcut a >> n  Right shift: a = a / 2^n
<<=	         a <<= 5	    a = a << 5''' # Left shift shortcut a << n  Left shift: a = a *2^n
a = 5
b =10
a |= b
print(f"Bitwise OR:{a} Left Shift:{5 << 1} Right Shift:{5>>1}")

# 4. Bitwise Operators 
'''And(&), OR(|), XOR(^), leftshift(<<),Rightshift(>>),Not(~)'''

# 5. Logical operators
"""and, or ,  not"""
#6. Memebership Operator
'''
Operator       Description	                                                                                          Example
in	           Returns True if it finds a variable in the specified sequence, false otherwise.	                      a in b
not in	       returns True if it does not finds a variable in the specified sequence and false otherwise.	          a not in b'''

l = [10,20,'r',40,'p']
print(f"is a present in list:{a in l} or if a not present in list:{a not in l}")

# 7. identity operator
'''Python identity operators compare the memory locations of two objects.
'''

a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
c = a

print(a is c)
print(a is b)

print(a is not c)
print(a is not b)


    