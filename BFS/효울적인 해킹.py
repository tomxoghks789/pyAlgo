# 1325

from collections import deque
import sys

def bfs(idx):
    counter = 1
    visited = [0] * (N + 1)
    visited[idx] = 1
    que = deque([idx])
    while que:
        now = que.popleft()
        for i in mapData[now]:
            if visited[i] == 0:
                counter += 1
                que.append(i)
                visited[i] = 1
    return counter

N, M = map(int, input().split())
mapData = [[] for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    mapData[b].append(a)

ans = []
max_cnt = 0
for i in range(1, N + 1):
    tempVal = bfs(i)
    if max_cnt == tempVal:
        ans.append(i)
    if max_cnt < tempVal:
        max_cnt = tempVal
        ans = []
        ans.append(i)
print(*ans)