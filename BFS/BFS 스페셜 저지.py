from collections import deque
import sys

N = int(input())
graph = [[] for _ in range(N + 1)]

def BFS():
    ans = []
    visited = [0] * (N + 1)
    queue = deque([1])
    while queue:
        node = queue.popleft()
        if not visited[node]:
            visited[node] = 1
            ans.append(node)
            queue.extend(graph[node])
    return ans

for _ in range(N - 1):
    V1, V2 = map(int, sys.stdin.readline().split())
    graph[V1].append(V2)
    graph[V2].append(V1)

ans = list(map(int,  sys.stdin.readline().split()))

if BFS() == ans:
    print(1)
else:
    print(0)