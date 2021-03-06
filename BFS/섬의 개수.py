# 4963번
from queue import Queue
import sys

direction = [[-1, 0], [1, 0], [0, 1], [0, -1], [-1, -1], [1, 1], [-1, 1], [1, -1]]

def bfs(x, y):
    que = Queue()
    que.put([x, y])
    visited[x][y] = 1

    while not que.empty():
        tx, ty = que.get()

        for i in range(len(direction)):
            nx = tx + direction[i][0]
            ny = ty + direction[i][1]
            if 0 <= nx < h and 0 <= ny < w:
                if mapData[nx][ny] and not visited[nx][ny]:
                    que.put([nx, ny])
                    visited[nx][ny] = 1

while True:
    counter =0
    w, h = map(int, input().split())
    if not h and not w:
        break
    mapData = [[0] * w for _ in range(h)]
    visited = [[0] * w for _ in range(h)]

    for i in range(h):
        temp = sys.stdin.readline().split()
        for j in range(w):
            mapData[i][j] = int(temp[j])

    for i in range(h):
        for j in range(w):
            if mapData[i][j] and not visited[i][j]:
                bfs(i, j)
                counter += 1

    print(counter)