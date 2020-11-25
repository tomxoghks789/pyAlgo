# 10797
import sys
ans = 0
N = sys.stdin.readline().strip()
N = N[-1]
car = list(map(str, sys.stdin.readline().strip().split()))
for i in range(5):
    if car[i][-1] == N:
        ans += 1
print(ans)

