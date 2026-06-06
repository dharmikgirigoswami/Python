#Operators 
# to perform operations on values and variables 

# 1) Arithmetic Operator 
# Arithmetic operators are used with numeric values to perform common mathematical operations:
'''
+	Addition	x + y	

-	Subtraction	x - y	

*	Multiplication	x * y	

/	Division	x / y	

%	Modulus	x % y	

**	Exponentiation	x ** y	

//	Floor division	x // y

'''
# Assignment Operator
# Assignment operators are used to assign values to variables

'''
Operator   Example	 Same As	
 =	       x = 5	 x = 5	
 +=	       x += 9	 x = x + 9	
 -=	       x -= 9	 x = x - 9	
 *=	       x *= 3	 x = x * 3	
 /=	       x /= 5	 x = x / 5	
 %=	       x %= 3	 x = x % 3	
 //=	   x //= 7	 x = x // 7	
 **=	   x **= 3	 x = x ** 3	
 &=	       x &= 3	 x = x & 3	
 |=	       x |= 3	 x = x | 3	
 ^=	       x ^= 3	 x = x ^ 3	
 >>=	   x >>= 3	 x = x >> 3	
 <<=	   x <<= 3	 x = x << 3	


'''
# The ternary operator in Python lets you write a conditional expression in one line. Its syntax is:
# value_if_true if condition else value_if_false

age = 20
status = "adult" if age >= 18 else "minor"
print(status)  # Output: adult


# Comparison Operators
# Comparison operators are used to compare two values:
'''
==	 Equal	                    x == y	
!=	 Not equal	                x != y	
>	 Greater than	            x > y	
<	 Less than	                x < y	
>=	 Greater than or equal to	x >= y	
<=	 Less than or equal to	    x <= y
'''

x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)


#Chaining Comparison Operators
# Python allows you to chain comparison operators:

x = 5
print(1 < x < 10)
print(1 < x and x < 10)

#Logical Operators
# Logical operators are used to combine conditional statements:

 
'''and 	 Returns True if both statements are true	                 x < 5 and  x < 10	
   or	 Returns True if one of the statements is true	             x < 5 or x < 4	
   not	 Reverse the result, returns False if the result is true	not(x < 5 and x < 10)'''

print(5 and 0)   # → 0  
print(5 or 0)    # → 5

#Identity Operators
#Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

'''
is 	    Returns True if both variables are the same object	    x is y	
is not	Returns True if both variables are not the same object	x is not y
'''

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)


#Bitwise Operators
#Bitwise operators are used to compare (binary) numbers:


'''
& 	AND	Sets each bit to 1 if both bits are 1	                                                                                 x & y	
|	OR	Sets each bit to 1 if one of two bits is 1	                                                                             x | y	
^	XOR	Sets each bit to 1 if only one of two bits is 1         	                                                             x ^ y	
~	NOT	Inverts all the bits	                                                                                                    ~x	
<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	                 x << 2	
>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	 x >> 2	

'''

print(6 & 3)

# Operator Precedence
# Operator precedence describes the order in which operations are performed.
'''

()	            Parentheses	
**	            Exponentiation	
+x  -x  ~x	    Unary plus, unary minus, and bitwise NOT	
*  /  //  % 	Multiplication, division, floor division, and modulus	
+  -	        Addition and subtraction	
<<  >>	        Bitwise left and right shifts	
&	            Bitwise AND	
^           	Bitwise XOR	
|	            Bitwise OR	
==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
not	            Logical NOT	
and	            AND	
or	            OR
'''

