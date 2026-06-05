# Strings 
# Strings in python are surrounded by either single quotation marks, or double quotation marks 
# 'hello' is the same as "hello".

print("Hello")
print('Hello')

#Quotes Inside Quotes
# You can use quotes inside a string, as long as they don't match the quotes surrounding the string:

print("It's alright")
print("He is called 'Johnny'")

# Assign String to a Variable
# Assigning a string to a variable is done with the variable name followed by an equal sign and the string:

a = "this is python"
print(a)

# Multiline Strings
# You can assign a multiline string to a variable by using three quotes:

a = """this is multiline string we can write multiple lines here"""

# Strings are Arrays

a = "hello world "
print(a[1])

# Looping Through a String
# Since strings are arrays, we can loop through the characters in a string, with a for loop.

for x in "banana":
  print(x)

# String Length
# To get the length of a string, use the len() function.

a = "Hello, World!"
print(len(a))

# Check String
# To check if a certain phrase or character is present in a string, we can use the keyword in.

txt = "The best things in life are free!"
print("free" in txt)

# Using if 

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")


# Check if NOT
# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

txt = "The best things in life are free!"
print("expensive" not in txt)

# Using if 
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

  