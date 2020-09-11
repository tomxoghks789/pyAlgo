import sys
x, y = map(int, input().split())
direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]
visited = [[0] * x for _ in range(y)]
mapData = [[0] * x for _ in range(y)]
counter = 0

for i in range(y):
    temp = sys.stdin.readline().split()
    for j in range(x):
        mapData[i][j] = int(temp[j])

print(mapData)