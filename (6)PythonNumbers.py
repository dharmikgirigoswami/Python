#Python Number 

x = 5 #int
y = 8.99 #float
z = 2j # complex 

# to print the type use 

print(type(x))
print(type(y))
print(type(z))

# Int 
# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

# Float
# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

 # Complex
# Complex numbers are written with a "j" as the imaginary part:

#Type conversion 
# To one type to another
x = 5 #int
y = 8.99 #float
z = 2j # complex 

# int to float 
a = float(x)

#float to int 
b  = int(y)

#int to complex
c = complex(x)


#Note: You cannot convert complex numbers into another number type.

#Random Number 

import random 
print(random.randrange(1,10))