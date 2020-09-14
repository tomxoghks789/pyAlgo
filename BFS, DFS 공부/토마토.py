# 7576번
from queue import Queue
import sys

x, y = map(int, input().split())
direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]
visited = [[0] * x for _ in range(y)]
mapData = [[0] * x for _ in range(y)]
scVisited = [[0] * x for _ in range(y)]
scMapData = [[0] * x for _ in range(y)]
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
        global counter
        c = qc.get()
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
        #             flag = 1
        # if flag == 1:
        #     global counter
        #     counter = c +1
        #     qc.put(c + 1)

def scan(i, j):
    que = Queue()
    que.put([i, j])
    scVisited[i][j] = 1
    while not que.empty():
        tx, ty = que.get()
        for i in range(len(direction)):
            nx = tx + direction[i][0]
            ny = ty + direction[i][1]
            if 0 <= nx < y and 0<= ny < x:
                if scMapData[nx][ny] == 0 and not scVisited[nx][ny]:
                    scVisited[nx][ny] = 1
                    scMapData[nx][ny] = 1
                    que.put([nx, ny])

#입력
for i in range(y):
    temp = sys.stdin.readline().split()
    for j in range(x):
        mapData[i][j] = int(temp[j])
        scMapData[i][j] = int(temp[j])


# 스캔
for i in range(y):
    for j in range(x):
        if scMapData[i][j] == 1 and not scVisited[i][j]:
            scan(i, j)


c = 0
for i in range(y):
    for j in range(x):
        if scMapData[i][j] == 1 or scMapData[i][j] == -1:
            c += 1

if scMapData == mapData:
    print(0)
elif c == y*x:
    print("계산")
    for i in range(y):
        for j in range(x):
            if mapData[i][j] and not visited[i][j]:
                bfs(i, j)
    print(counter)
    print(mapData)
else:
    print(-1)