squares = []
for x in range(10):
    squares.append(x * x)
print(squares[::])

square = [x * x for x in range(10) if x % 2]
print(square[:10])
##################

a, b, c = [10, 20, 30]
print(a, b, c)

a, b, *rest = [10,20,30,40,50,60]
print(a, b, rest)
###################

x, y = 5, 10
x, y = y, x
print(f"{x}, {y}")
###################

with open("data.text", "w") as f:
    idea = "Mark Elliot Zuckerberg\n"
    f.write(idea)
    
with open("data.text", "r") as f:
    content = f.read()
    print(content)
###################

class Example:
    def __enter__(self):
        print("opened")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("closed")
        
with Example() as e:
    print("Inside")
#####################

class Car:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed
    
    def drive(self):
        print(f"{self.brand} goes at speed of {self.speed}")
    
myCar = Car("Tesla CyberPunk", 200)
myCar.drive()
######################

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    # property allows a method to be accessed like an attribute
    @property
    def balance(self):
        return self._balance # no recursion

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value

u = BankAccount(20)
u.balance = -10 
print(u.balance)
###################

names = ["Elon", "Mark", "Jeff bezos", "Sam altman", "Alexandr Wang"]

for index, name in enumerate(names):
    print(index+1, name)
####################

digits = [1,2,3,4,5,6]
letters = ["a", "b", "c", "d", "e", "f", "g"]

for digit, letter in zip(digits, letters):
    print(digit, letter)
####################

nums = [1, 4, -2, 7]
has_negative = any(x<0 for x in nums)
print(has_negative) # true

all_positive = all(x>0 for x in nums)
print(all_positive) # false
######################

total = sum(x * x for x in range(10))
print(total)
######################
"""
instead of a type(x) == ...
"""
value = 10

if isinstance(value,int):
    print("this is an integer")
#######################

class Person:
    def __init__(self, name):
        self.name = name

p = Person("X-Ashe")
p.age = 19
age = getattr(p, "age", "Not found")
print(age)
########################

students = [{"name": "X", "score": 100},
            {"name": "Y", "score": 80},
            {"name": "Z", "score": 75}
           ]

sorted_students = sorted(students, key=lambda x: x["score"])
print(sorted_students)
##########################

square = lambda x: x * x
print(square(6))
##########################

def logger(func):
    def wrapper(*var, **vars):
        print("function started")
        func(*var, **vars)
        print("function ended")
    return wrapper

@logger
def greet(*args):
    print("{0}-{1}-{2}".format(*args))

greet("MacOS", "Windows", "Linux")
###########################

def show(*args, **kwargs):
    print(args) # collects any number of keyword arguments into a tuple
    print(kwargs) # collects any number of keyword arguments into a dictionary

show(1,2,3, name = "Rick", age = 30)