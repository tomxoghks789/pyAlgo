import sys
from queue import Queue

def BFS():
    counter = 0
    que = Queue()
    que.put([0, 0, 0])
    visited[0][0] = True
    while not que.empty():
        tx, ty, tc = que.get()
        if visited[tx][ty]:
            continue
        counter = tc
        if K != 0:
            for i in range(len(kDirection)):
                nx = tx + kDirection[i][0]
                ny = ty + kDirection[i][1]
                if 0<= nx < H and 0 <= ny < W:
                    if not data[nx][ny] and not visited[nx][ny]:
                        que.put([nx, ny, tc +1])
                        visited[nx][ny]
                        K = K - 1
        else:
            for i in range(len(direction)):
                nx = tx + direction[i][0]
                ny = ty + direction[i][1]
                if 0<= nx < H and 0 <= ny < W:
                    if data[nx][ny] and not visited[nx][ny]:
                        que.put([nx, ny, tc +1])
                        visited[nx][ny] = 1
    return counter

direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]
kDirection = [[-1, -2], [-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2]]

K = input()
W, H = map(int, input().split())
data = []
visited = [[False] * W for _ in range(H)]
print(visited)
for _ in range(H):
    data.append(list(map(int, sys.stdin.readline().split())))
print(BFS())
