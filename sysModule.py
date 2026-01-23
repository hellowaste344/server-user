import sys 
print(sys.version)
print(sys.path)

# sys.path = []
# will raise an error pandas 
# cannot be found if sys.path is emptied
import pandas as pd 

print(sys.modules)

for line in sys.stdin:
    print(f'input : {line}')
    if 'q' == line.rstrip():
        break
print("exit")

sys.stdout.write("Ashe\n")

def fun(*args):
    print(*args, file=sys.stderr)

fun("Error!")

n = len(sys.argv)

print("total arguments passed:", n)
print("name of python script", sys.argv[0])
print("arguments passed:", end=" ")

for i in range(1, n):
    print(sys.argv[i], end=" ")

Sum = 0
for i in range(1,n):
    Sum += int(sys.argv[i])

print("\n",Sum)

age = 17
if age < 18:
    sys.exit("age less than 18")
else:
    print("age is not less than 18")

a = "age"
print(sys.getrefcount(a))