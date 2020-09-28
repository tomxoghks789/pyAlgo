import sys
N = int(input())

def DFS(i):
    visited[i] = True
    for ni in graph[i]:
        if visited[ni] is False:
            DFS(ni)

for _ in range(N):
    counter = 0
    M = int(input())
    graph = [[] for _ in range(M + 1)]
    visited = [False] * (M + 1)
    data = list(map(int, sys.stdin.readline().split()))
    for i in range(1, len(data) + 1):
        graph[i].append(data[i - 1])
    for i in range(1, M + 1):
        if visited[i] is False:
            DFS(i)
            counter += 1
    print(counter)