from collections import deque

kDirection = [[-1, -2], [-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2]]

def BFS(startX, startY, endX, endY, visited):
    que = deque()
    que.append([startX, startY, 0])
    visited[startX][startY] = 1
    while que:
        cx, cy, cc = que.popleft()
        if cx == endX and cy == endY:
            print(cc)
            break
        for i in range(len(kDirection)):
            nx = cx + kDirection[i][0]
            ny = cy + kDirection[i][1]
            if -1 < nx < L and -1 < ny < L and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                que.append([nx, ny, cc + 1])

N = int(input())

for _ in range(N):
    L = int(input())
    visited = [[0] * L for _ in range(L)]
    x, y = map(int, input().split())
    targetX, targetY = map(int, input().split())
    BFS(x, y, targetX, targetY, visited)