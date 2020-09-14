# 4963번
from queue import Queue
import sys

direction = [[-1, 0], [1, 0], [0, 1], [0, -1], [-1, -1], [1, 1], [-1, 1], [1, -1]]

def bfs(x, y):
    que = Queue()
    que.put([x, y])
    while not que.empty():
        tx, ty = que.get()
        for i in range(len(direction)):
            nx = tx + direction[i][0]
            ny = ty + direction[i][1]
            if 0 <= nx < y and 0 <= ny < x:
                if mapData[nx][ny] and not visited[nx][ny]:
                    que.put([nx, ny])
                    visited[nx][ny] = 1

while True:
    counter =0
    x, y = map(int, input().split())
    if not x and not y:
        break
    mapData = [[0] * x for _ in range(y)]
    visited = [[0] * x for _ in range(y)]
    for i in range(y):
        temp = sys.stdin.readline().split()
        for j in range(x):
            mapData[i][j] = int(temp[j])
    for i in range(y):
        for j in range(x):
            if mapData[i][j] and not visited[i][j]:
                bfs(i, j)
                counter += 1
    print(counter)