from queue import Queue

N, M = map(int, input().split())
mapData = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]
counter = []

def bfs(x, y):
    que = Queue()
    que.put([x,y])
    visited[x][y] = 1
    count = 1
    while not que.empty():
        x, y = que.get()
        for i in range(len(direction)):
            nx = x + direction[i][0]
            ny = y + direction[i][1]
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and mapData[nx][ny]:
                    que.put([nx, ny])
                    count = count + 1
                    visited[nx][ny] = 1
    counter.append(count)

for i in range(N):
    for j in range(M):
        if mapData[i][j] and not visited[i][j]:
            bfs(i, j)

if not counter:
    print(0)
    print(0)
else:
    print(len(counter))
    print(max(counter))
