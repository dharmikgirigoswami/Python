 # this all are variable use to store some values 
x = 99
y = "this is python "
z = 2.34


# casting (to specify the data type of variable )
u = str(3)
t = float(22.33)


#Get the type 
i=24
p=33
print(type(i))
print(type(p))


#Case Sensetive
a=22
A="hello" 
#both are valid 

#legal variable names 
my_var=22
MyVar=56
myvar=33

#multi words variable names 
#Camel Case
#Each word, except the first, starts with a capital letter:

myVariableName = "John"


#Pascal Case
#Each word starts with a capital letter:

MyVariableName = "John"

#Snake Case
#Each word is separated by an underscore character:

my_variable_name = "John"

#Assign multiple values 
x,y,z = 'mango','banana','orange'
print(x)
print(y)
print(z)


#one value to multiple variables 
x=y=z='orange'
print(x)
print(y)
print(z)


#unpack a collection 

fruits = ["mango","watermelon","banana"]
x,y,z=fruits
print(x)
print(y)
print(z)


#output variable 
x=3
print(x)

#for multiple values we use , or +
x="hello" 
y="this"
z="is python"

print(x,y,z)
print(x+y+z)


#to print string and a number together we use ,
x=5
y="hello"
print(x,y)


#global variable 
# variable that is created outside the function 
x='cool'

def myfunc():
    print("python is " + x)

myfunc()

#global keyword 
def myfunc():
    global x 
    x ="FANSTASTIC"

    myfunc()
    
    print("python is "+ x)
    



    