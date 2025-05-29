
from collections import deque

q = deque()
q.append(10)
q.append(20)
q.append(30)

print('Initial queue : ',q)
print(q.popleft())
print(q.popleft())
print(q.popleft())

print('After remove queue : ',q)