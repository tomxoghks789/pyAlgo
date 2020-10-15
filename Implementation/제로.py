# 10773번
import sys
N = int(sys.stdin.readline())
ans = []
for i in range(N):
    temp = int(sys.stdin.readline())
    if temp == 0:
        ans.pop()
    else:
        ans.append(temp)
print(sum(ans))