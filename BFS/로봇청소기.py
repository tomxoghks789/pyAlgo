from queue import Queue
import sys
# .: 깨끗한 칸
# *: 더러운 칸
# x: 가구
# o: 로봇 청소기의 시작 위치

direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    mapData = [[None] * w for _ in range(h)]
    # 입력
    for i in range(h):
        temp = sys.stdin.readline()
        for j in range(w):
            mapData[i][j] = temp[j]
    print(mapData)
    for i in range(len(mapData)):
        if '*' in mapData[i]:
            print(-1)
            break
