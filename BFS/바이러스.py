from collections import deque

def bfs(graph):
    visited = []
    que = deque([1])
    while que:
        t = que.popleft()
        if t in visited:
            continue
        if not t in visited:
            visited.append(t)
            que.extend(sorted(graph[t]))
    if len(visited) == 1:
        return 1
    else:
        return len(visited) - 1

N = int(input())
M = int(input())

graph = [set([]) for _ in range(N + 1)]

for _ in range(M):
    V1, V2 = map(int, input().split())
    graph[V1].add(V2)
    graph[V2].add(V1)

print(bfs(graph))