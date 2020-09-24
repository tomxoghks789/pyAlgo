import sys
from collections import deque

def bfs():
    visited[0][0][1] = 1
    que = deque()
    que.append([0, 0, 1])
    while que:
        x, y, k = que.popleft()
        if x == N - 1 and y == M - 1:
            return visited[x][y][k]

        for i in range(len(direction)):
            nx = x + direction[i][0]
            ny = y + direction[i][1]

            if 0 <= nx < N and 0 <= ny < M:
                if k and mapData[nx][ny] and not visited[nx][ny][k - 1]:
                    que.append((nx, ny, k - 1))
                    visited[nx][ny][k - 1] = visited[x][y][k] + 1

                if not mapData[nx][ny] and not visited[nx][ny][k]:
                    que.append((nx, ny, k))
                    visited[nx][ny][k] = visited[x][y][k] + 1
    return -1

direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]
N, M = map(int, input().split())
mapData = [[0] * M for _ in range(N)]
visited = [[[0 for i in range(2)] for i in range(M)] for i in range(N)]

for i in range(N):
    temp = sys.stdin.readline()
    for j in range(M):
        mapData[i][j] = int(temp[j])

print(bfs())