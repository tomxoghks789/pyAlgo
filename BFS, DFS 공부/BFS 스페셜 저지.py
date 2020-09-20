from collections import deque
import sys

N = int(input())
graph = [[] for _ in range(N + 1)]
visited = []

def BFS():
    queue = deque([1])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(sorted(graph[node]))
    if visited == ans:
        print(1)
    else:
        print(0)

for i in range(N - 1):
    V1, V2 = map(int, sys.stdin.readline().split())
    graph[V1].append(V2)
    graph[V2].append(V1)

ans = list(map(int, input().split()))

BFS()
