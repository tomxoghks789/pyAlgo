from queue import  Queue

def BFS(x, y):
    que = Queue()
    que.put([x, y]) # Queue 초기화시에 put 금지
    visited[x][y] = 1
    while not que.empty():
        tx, ty = que.get()
        for i in range(len(direction)):
            nx = tx + direction[i][0]
            ny = ty + direction[i][1]
            if 0 <= nx < h and 0 <= ny < w:
                if not visited[nx][ny] and mapData[nx][ny]:
                    que.put([nx, ny])
                    visited[nx][ny] = 1
    counter.append(0)

N = int(input())
for _ in range(N):
    w, h, k = map(int, input().split())
    mapData = [[0] * w for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    counter = []

    for _ in range(k):
        y, x = map(int, input().split())
        mapData[x][y] = 1

    for i in range(h):
        for j in range(w):
            if mapData[i][j] and not visited[i][j]:
                BFS(i, j)

    print(len(counter))