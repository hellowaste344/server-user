def simpleYieldfunc():
    yield 1
    yield 2
    yield 3

# iterate the each value 
for v in simpleYieldfunc():
    print(v, end=" ")

def infSquare():
    i = 1

    while True:
        yield i*i
        i += 1

# let's check a few output
for num in infSquare():
    if num > 100:
        break
    print(num, end=" ")