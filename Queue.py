# logic of Queue: First in, First out FIFO
from queue import Queue
q = Queue(maxsize=3)
print("initial size:", q.qsize())
q.put('a')
q.put('b')
q.put('c')
print("Is full:", q.full())

for i in range(q.qsize()):
    print(q.get())
print("Is empty:", q.empty())

print("Queue: ", q)