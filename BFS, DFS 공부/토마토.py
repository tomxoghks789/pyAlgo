# 7576번
from queue import Queue
import sys

counter = 0

x, y = map(int, input().split())
direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]
visited = [[0] * x for _ in range(y)]
mapData = [[0] * x for _ in range(y)]
counter = 0

def bfs(i, j):
    que = Queue()
    que.put([i, j])
    visited[i][j] = 1
    qc = Queue()
    qc.put(0)
    while not que.empty():
        flag = 0
        tx, ty = que.get()
        c = qc.get()
        global counter
        counter = c
        for i in range(len(direction)):
            nx = tx + direction[i][0]
            ny = ty + direction[i][1]
            if 0 <= nx < y and 0<= ny < x:
                if mapData[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    mapData[nx][ny] = 1
                    que.put([nx, ny])
                    qc.put(c + 1)

#입력
for i in range(y):
    temp = sys.stdin.readline().split()
    for j in range(x):
        mapData[i][j] = int(temp[j])

# 시작
for i in range(y):
    for j in range(x):
        if mapData[i][j] and not visited[i][j]:
            bfs(i, j)

print(counter)
print(mapData)
print(visited)


# if 0 <= nx < x and 0 <= ny < y:
#     print(nx, ny)
