# 11659
import sys
N, M = map(int, sys.stdin.readline().split())

inputData = list(map(int, sys.stdin.readline().split()))
ans = [inputData[0]]
for i in range(1, N):
    ans.append(ans[i - 1] + inputData[i])

for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    if x == 1:
        print(ans[y - 1])
    else:
        print(ans[y - 1] - ans[x - 2])