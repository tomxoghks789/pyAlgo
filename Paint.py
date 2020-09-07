from collections import deque

N, M = map(int, input().split())

mapData = [list(map(int, input().split())) for i in range(N)]
visited = [[0] * M for _ in range(N)]

direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]
counter = []


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
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 0 and mapData[nx][ny]:
                    qx.append(nx)
                    qy.append(ny)
                    count = count + 1
                    visited[nx][ny] = 1
    counter.append(count)


# 돌려
for i in range(N):
    for j in range(M):
        if mapData[i][j] and not visited[i][j]:
            bfs(i, j)

if not counter:
    counter.append(0)

print(len(counter))
print(max(counter))