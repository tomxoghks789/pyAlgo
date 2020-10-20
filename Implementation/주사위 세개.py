# 2480
import sys
N = list(map(int, sys.stdin.readline().split()))
ans = 0
temp = 0
N.sort()
front = N[0]
back = N[1]
if back > front:
    front = back
x = N.count(front)
if x == 3:
    temp = 10000 + front * 1000
if x == 2:
    temp = 1000 + front * 100
if N[0] != N[1] != N[2]:
    temp = max(N) * 100
if ans < temp:
    ans = temp
print(ans)