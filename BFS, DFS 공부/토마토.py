# 7576번
from queue import Queue
import sys

counter = 0

def bfs(x, y):
    que = Queue()
    que.put([x, y])
    visited[x][y] = 1
    while not que.empty():
        tx, ty = que.get()
        for i in range(len(direction)):
            nx = tx + direction[i][0]
            ny = ty + direction[i][1]
            if -1 < nx < y and -1 < ny < x:
                visited[nx][ny] = 1
                que.put([nx, ny])
        global  counter
        counter += 1

x, y = map(int, input().split())
direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]
visited = [[0] * x for _ in range(y)]
mapData = [[0] * x for _ in range(y)]

#입력
for i in range(y):
    temp = sys.stdin.readline().replace(" ", "")
    for j in range(x):
        mapData[i][j] = int(temp[j])

# 시작
for _ in range(2):
    for i in range(y):
        for j in range(x):
            if mapData[i][j] and not visited[i][j]:
                bfs(i, j)
print(counter)