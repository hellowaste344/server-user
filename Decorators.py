def hi(name = "Smash"):
   return "hi {0}".format(name)

greet = hi
print(greet())

del hi
# print(hi()) 
# gives error
#########################

def hi(name="Sukuna"):
    def greet():
        return "hi you are in greet() function"
    def welcome():
        return "now you are in welcome() function"
    
    if(name != "Sukuna"):
        return greet # don't put paranthesis cause with () program will execute the function
    else: 
        return welcome # don't put paranthesis cause with () program will execute the function
    
a = hi()
print(a) #<function hi.<locals>.welcome at 0x00000253C533CA40> points the welcome()
print(a()) #output welcome() 
del hi
###########################

def hi():
    return "hi world"

def doSomethingbeforeHi(func):
    print("I am doing some boring work before executing hi()")
    print(func())
    
doSomethingbeforeHi(hi)    
#############################
def a_New_decorator(func):
    def wrapperFunction(*args):
        print("I am doing some wrapping process")
        
        func(*args)
        
        print("I am ending some wrapping process")
    return wrapperFunction


def function_Needs_decoration(*args):
    print("I am the function needs some decoration {0}".format(args))
    
Decorated = a_New_decorator(function_Needs_decoration)
Decorated("X")

@a_New_decorator
def function_needs_decoration(*var):
    print("I am the second function needs some decoration{0}".format(var))
    
function_needs_decoration("X")