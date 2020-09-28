import sys
sys.setrecursionlimit(10000000)

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

def DFS(i):
    visited[i] = True
    for ni in graph[i]:
        if visited[ni] is False:
            DFS(ni)

for _ in range(M):
    V1, V2 = map(int, sys.stdin.readline().split())
    graph[V1].append(V2)
    graph[V2].append(V1)

counter = 0

for i in range(1, N + 1):
    if visited[i] is False:
        DFS(i)
        counter += 1

print(counter)