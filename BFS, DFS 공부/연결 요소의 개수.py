from collections import deque

def BFS():
    counter = 0
    nodes =  list(range(1, N + 1))
    visited = []
    que = deque()
    while len(nodes) != 0:
        que.append(nodes[0])
        while que:
            node = que.popleft()
            if node in visited:
                continue
            nodes.remove(node)
            if node not in visited:
                visited.append(node)
                que.extend(sorted(graph[node]))
        counter += 1
    return counter


N, M = map(int, input().split())
graph = [set([]) for i in range(N + 1)]

for _ in range(M):
    V1, V2 = map(int, input().split())
    graph[V1].add(V2)
    graph[V2].add(V1)

print(BFS())