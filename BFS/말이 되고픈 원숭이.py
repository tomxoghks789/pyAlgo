import sys
from collections import deque

K = int(input())
W, H = map(int, input().split())
data = []
visited = [[[0 for i in range(K + 1)] for i in range(W)] for i in range(H)]

def BFS():
    counter = 0
    que = deque()
    que.append((0, 0, K))
    visited[0][0][0] = 1

    while que:
        tx, ty, tk = que.popleft()

        if tx == H - 1 and ty == W - 1:
            return visited[tx][ty][tk]

        if tk > 0:
            for i in range(len(kDirection)):
                nx = tx + kDirection[i][0]
                ny = ty + kDirection[i][1]
                if 0 <= nx < H and 0 <= ny < W and not data[nx][ny] and not visited[nx][ny][tk - 1]:
                        que.append((nx, ny, tk - 1))
                        visited[nx][ny][tk - 1] = visited[tx][ty][tk] + 1

        for i in range(len(direction)):
            nx = tx + direction[i][0]
            ny = ty + direction[i][1]
            if 0 <= nx < H and 0 <= ny < W and not data[nx][ny] and not visited[nx][ny][tk]:
                    que.append((nx, ny, tk))
                    visited[nx][ny][tk] = visited[tx][ty][tk] + 1
    return -1

direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]
kDirection = [[-1, -2], [-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2]]

for _ in range(H):
    data.append(list(map(int, sys.stdin.readline().split())))

print(BFS())