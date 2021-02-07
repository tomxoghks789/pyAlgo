# 18352

from collections import deque
import sys
N, M, K, X = map(int, sys.stdin.readline().split())
visited = [-1] * (N + 1)
visited[X] = 0
mapData = [[] for _ in range(N + 1)]

for i in range(M):
    V1, V2 = map(int, sys.stdin.readline().split())
    mapData[V1].append(V2)

print(mapData)
que = deque([X])
while que:
    now = que.popleft()
    for nxt in mapData[now]:
        if visited[nxt] == -1:
            visited[nxt] = visited[now] + 1
            que.append(nxt)
for i in range(N + 1):
    if visited[i] == K:
        print(i)
print(visited)
if K not in visited:
    print(-1)