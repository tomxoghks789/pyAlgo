# 11725

from collections import deque
import sys
N = int(input())

ans = [0] * (N + 1)
mapData = [[] for _ in range(N + 1)]

for i in range(N - 1):
    V1, V2 = map(int, sys.stdin.readline().split())
    mapData[V1].append(V2)
    mapData[V2].append(V1)

que = deque([1])
visited = [0] * (N + 1)

while que:
    now = que.popleft()
    for i in mapData[now]:
        if not visited[i]:
            ans[i] = now
            que.append(i)
            visited[i] = 1
for i in ans[2:]:
    print(i)

