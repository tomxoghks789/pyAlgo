import sys

N = int(input())

mapData = [[0] * N for _ in range(N)]

for i in range(N):
    temp = sys.stdin.readline()
    for j in range(N):
        mapData[i][j] = int(temp[j])

visited = [[0 for _ in range(N)] for _ in range(N)]
