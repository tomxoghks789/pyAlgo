# 백준 2667 단지번호붙이기

import sys
from collections import deque

N = int(input())

mapData = [[0] * N for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]

direction = [[-1, 0], [0, -1], [1, 0], [0, 1]]
counter = []


def bfs(x, y):
    qx = deque([x])
    qy = deque([y])
    count = 0
    while qx:
        x = qx.popleft()
        y = qy.popleft()
        if check(x, y) == 0:
            continue
        count = count + 1
        visited[x][y] = 1
        for i in range(len(direction)):
            nx = x + direction[i][0]
            ny = y + direction[i][1]
            qx.append(nx)
            qy.append(ny)
    counter.append(count)


def check(x, y):
    if x < 0 or y < 0 or x >= N or y >= N or mapData[x][y] == 0 or visited[x][y] == 1:
        return 0
    else:
        return 1


# 입력
for i in range(N):
    temp = sys.stdin.readline()
    for j in range(N):
        mapData[i][j] = int(temp[j])

# 돌려
for i in range(N):
    for j in range(N):
        if check(i, j):
            bfs(i, j)

print(len(counter))
counter = sorted(counter)
for i in range(len(counter)):
    print(counter[i])