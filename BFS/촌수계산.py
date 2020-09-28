from collections import deque

N = int(input())
start, end = map(int, input().split())
M = int(input())
graph = [set([]) for i in range(N + 1)]

def bfs(graph, start, end):
    visited = []
    que = deque([start])
    qc = deque([0])
    counter = 0
    while que:
        node = que.popleft()
        c = qc.popleft()
        if node in visited:
            continue
        if node == end:
            counter = c
            break
        if node not in visited:
            visited.append(node)
            que.extend(sorted(graph[node]))
            for _ in range(len(graph[node])):
                qc.append(c + 1)

    if counter == 0:
        counter = -1

    return counter


for i in range(M):
    V1, V2 = map(int, input().split())
    graph[V1].add(V2)
    graph[V2].add(V1)

print(bfs(graph, start, end))
