# 2566
import sys
data = []
for i in range(9):
    data.append(list(map(int, sys.stdin.readline().strip().split())))

maxVal = 0
maxPoint = [0, 0]
for i in range(9):
    for j in range(9):
        if data[i][j] > maxVal:
           maxVal = data[i][j]
           maxPoint = [i, j]

print(maxVal)
print(maxPoint[0] + 1, maxPoint[1] + 1)