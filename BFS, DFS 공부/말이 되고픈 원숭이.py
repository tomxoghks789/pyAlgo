import sys
from queue import Queue

K = int(input())
W, H = map(int, input().split())
data = []
visited = [[0] * W for _ in range(H)]

def BFS():
    counter = 0
    que = Queue()
    que.put([0, 0, 0, K])
    visited[0][0] = 1

    while not que.empty():
        tx, ty, tc, tk = que.get()
        counter = tc

        if tx == H - 1 and ty == W - 1:
            return counter

        if tk > 0:
            for i in range(len(kDirection)):
                nx = tx + kDirection[i][0]
                ny = ty + kDirection[i][1]
                if 0 <= nx < H and 0 <= ny < W:
                    if not data[nx][ny] and not visited[nx][ny]:
                        que.put([nx, ny, tc +1, tk - 1])
                        visited[nx][ny] = 1

        for i in range(len(direction)):
            nx = tx + direction[i][0]
            ny = ty + direction[i][1]
            if 0 <= nx < H and 0 <= ny < W:
                if not data[nx][ny] and not visited[nx][ny]:
                    que.put([nx, ny, tc + 1, tk])
                    visited[nx][ny] = 1
    return -1

direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]
kDirection = [[-1, -2], [-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2]]

for _ in range(H):
    data.append(list(map(int, sys.stdin.readline().split())))

print(BFS())