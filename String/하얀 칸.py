# 1100

mapData = []
for i in range(8):
    mapData.append(input())
ans = 0
startColor = 0
for i in range(8):
    for j in range(startColor, 8, 2):
        if mapData[i][j] == 'F':
            ans += 1
    startColor = not startColor
print(ans)