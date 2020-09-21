import sys
from queue import Queue

K =int(input())
W, H = map(int, input().split())
data = []
visited = [[0] * W for _ in range(H)]

def BFS(K):
    flag = 0
    counter = 0
    que = Queue()
    que.put([0, 0, 0])
    visited[0][0] = 1
    while not que.empty():
        tx, ty, tc = que.get()
        counter = tc
        if tx == H - 1 and ty == W - 1:
            flag = 1
            break
        if K > 0:
            for i in range(len(kDirection)):
                # 여기에 가는길에 뭐 없나 체크
                nx = tx + kDirection[i][0]
                ny = ty + kDirection[i][1]
                if 0<= nx < H and 0 <= ny < W:
                    if not data[nx][ny] and not visited[nx][ny]:
                        que.put([nx, ny, tc +1])
                        visited[nx][ny] = 1
                        K = K - 1
        else:
            for i in range(len(direction)):
                nx = tx + direction[i][0]
                ny = ty + direction[i][1]
                if 0<= nx < H and 0 <= ny < W:
                    if not data[nx][ny] and not visited[nx][ny]:
                        que.put([nx, ny, tc +1])
                        visited[nx][ny] = 1
    if flag == 0:
        return -1
    return counter

direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]
kDirection = [[-1, -2], [-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2]]
spaceDirection = [[]]

for _ in range(H):
    data.append(list(map(int, sys.stdin.readline().split())))
print(BFS(K))