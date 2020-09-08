from collections import deque
import sys

N = int(input())

mapData = [[0] * N for _ in range(N)]
visited = [[0] * N for _ in range(N)]
direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]
counter = []

for i in range(N):
    temp = sys.stdin.readline()
    for j in range(N):
        mapData[i][j] = int(temp[j])

def bfs(x, y):
    qx = deque([x])
    qy = deque([y])
    visited[x][y] = 1
    count = 1

    while qx:
        x = qx.popleft()
        y = qy.popleft()

        for i in range(len(direction)):

            nx = x + direction[i][0]
            ny = y + direction[i][1]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0 and mapData[nx][ny]:
                    qx.append(nx)
                    qy.append(ny)
                    count = count + 1
                    visited[nx][ny] = 1
    counter.append(count)


# 돌려
for i in range(N):
    for j in range(N):
        if mapData[i][j] and not visited[i][j]:
            bfs(i, j)


print(len(counter))
counter = sorted(counter)
for i in range(len(counter)):
    print(counter[i])
