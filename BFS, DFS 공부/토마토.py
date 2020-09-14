# 7576번
from collections import deque
import sys

x, y = map(int, input().split())
direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]
mapData = [[0] * x for _ in range(y)]

def bfs(tQ):
    counter = -1
    while tQ:
        counter += 1
        for _ in range(len(tQ)):
            tx, ty = tQ.popleft()
            for i in range(len(direction)):
                nx = tx + direction[i][0]
                ny = ty + direction[i][1]
                if 0 <= nx < y and 0<= ny < x:
                    if mapData[nx][ny] == 0:
                        mapData[nx][ny] = 1
                        tQ.append([nx, ny])
    return counter


tempQue = deque()

#입력
for i in range(y):
    temp = sys.stdin.readline().split()
    for j in range(x):
        tempVal = int(temp[j])
        mapData[i][j] = tempVal
        if tempVal == 1:
            tempQue.append([i, j])

result = bfs(tempQue)
flag = 0
for i in range(y):
    if mapData[i].count(0) >= 1:
        result = -1
        break
if not flag:
    print(result)