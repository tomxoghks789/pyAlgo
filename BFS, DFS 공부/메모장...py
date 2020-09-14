from collections import deque

temp = deque()
temp.append([3, 4])
temp.append([6, 7])
print(temp)
x, y = temp.popleft()
print(x, y)