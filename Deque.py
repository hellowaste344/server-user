from collections import deque

dq = deque([20,30,40])

dq.appendleft(10)
dq.append(50)

dq.extend([60,70,80])

print(' '.join(map(str, dq)))

dq.popleft()
dq.pop()
dq.remove(50)

dq.rotate(2) # rotate the deque steps to the right
dq.reverse()

print(' '.join(map(str, dq)))
print(dq.count(20))

dq.clear() # deque: []