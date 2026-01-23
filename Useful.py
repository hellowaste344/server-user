def do_twice(func):
    # you can use *var, *vars instead of *args, **kwargs -> conventional
    def wrapper_do_twice(*var, **vars): 
        func(*var, **vars)
        func(*var, **vars)
    return wrapper_do_twice

@do_twice
def greet(name):
    print(f"hello, {name}!")
    
greet("world")
#######################
def function_arg(f_arg,*argv):
    print(f"first normal arg: {f_arg}")
    for arg in argv:
        print("another arguments through argv: ", arg)
        
output = function_arg("school", "apple", "GPU", "TSMC")
print(output)
#######################
def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0}->{1}".format(key, value))
        
greet_me(name="Satoshi", place= "tokyo") # use "=" instead of ":" when passing **keywordargs
#######################
def function_call(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)
    
args = ("random", 1, 3)
function_call(*args) 

kwargs = {"arg1": 5, "arg2":"apple", "arg3": 1}
function_call(**kwargs)
#######################
x = {'a': 1, 'b': 4}
y = {'c': 5, 'b': 3}

z = {**x , **y}

print(z)
#######################
a = [12,32,4235,24,56]

for i in range(len(a)):
    #default print ends with "\n"
    print(a[i], end = " ")#end = " " declares a space between outputs 

a[0] = 100
a.append(999)
print("\nModified array:")
print(sorted(a))
#########################
import array as arr
a = arr.array('i', [10, 20, 30, 40, 50])#'i' represents integer array not an item!

for i in a:
    print(i, end = " ")
##########################
import numpy as np

a = np.array([10,20,30,40,50,50])
print("1D Array:", a)

b = np.array([[1,2,3], [4,5,6]])
print("2D Array:", b)
##########################
a = [x**2 for x in range(1, 11)]
print(a)