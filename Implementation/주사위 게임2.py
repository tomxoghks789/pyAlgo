# 10103
import sys
N = int(sys.stdin.readline())
x = 100
y = 100

for _ in range(N):
    t1, t2 = map(int, sys.stdin.readline().split())
    if t1 > t2:
        y -= t1
    elif t1 == t2:
        continue
    else:
        x -= t2
print(x)
print(y)