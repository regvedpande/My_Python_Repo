#Default Argument
#In this case, if no values are provided, a=9 and b=1 will be used by default
#Here both arguments are provided (8,4), so default values are not used
def Argue(a = 9, b = 1):
    print("Sum of two numbers", a + b)
    
Argue(8, 4)

#Default Argument
#Same function as above, but only one argument is provided
#Here a=8 (provided) and b=1 (uses default value)
def Argue(a = 9, b = 1):
    print("Sum of two numbers", a + b)
    
Argue(8)

#Keyword Argument
#Arguments are passed using parameter names (keywords)
#This makes the order of arguments flexible
#Here we explicitly specify which value goes to which parameter
def Argue3(a = 9, b = 4):
    print("Sum of two numbers", a + b)
    
Argue3(b = 8, a = 4)

#Required Argument
#Parameters without default values are required arguments
#Here 'a' and 'b' must be provided, while 'c' is optional with default value 1
#If 'c' is not provided, it uses default value 1
def Argue4(a, b, c = 1):
    print("Sum of two numbers", (a + b + c)/3)
    
Argue4(8, 4)  #c will use default value 1


#Variable-length Argument
#This function can take any number of arguments
#The '*' symbol is used to pass a variable number of arguments
#The arguments are stored in a tuple
def Argue5(*args):
    print("Sum of two numbers", sum(args))
    
Argue5(8, 4, 5, 6, 7, 8, 9, 10)


#Variable-length Keyword Argument
#This function can take any number of keyword arguments 
#The '**' symbol is used to pass a variable number of keyword arguments
#The arguments are stored in a dictionary
def Argue6(**kwargs):
    print("Sum of two numbers", sum(kwargs.values()))
    
Argue6(a = 8, b = 4, c = 5, d = 6, e = 7, f = 8, g = 9, h = 10)