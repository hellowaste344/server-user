import operator
import time

a = list(range(1,10001))
b = list(range(1,10001))

num_iterations = 5
mapt = []
loopt = []

def mapfunc():
    for _ in range(num_iterations):
        t1 = time.time()
        result = list(map(operator.mul, a, b))
        t2 = time.time()
        mapt.append(t2-t1)

for _ in range(num_iterations):
    t1 = time.time()
    result = [a[i] * b[i] for i in range(len(a))]
    t2 = time.time()
    loopt.append(t2-t1)

avg_mapt = sum(mapt) / num_iterations
avg_loopt = sum(loopt) / num_iterations

print(f"Average time of map:{avg_mapt:.6f}")
print(f"Average time of for loop:{avg_loopt:.6f}")

from itertools import count 

for number in count(start=1, step=2):
    if number > 10:
        break
    print(number)

import itertools

l = ["MIT", "Harvard", "Stanford"]

# defining iterator
iterators = itertools.cycle(l)

for i in range(6):
    print(next(iterators), end=" ")

count = 0

from itertools import permutations
print(list(permutations([1, "MIT"], 2)))
