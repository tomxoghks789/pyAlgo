# 1913

N = int(input())
findNum = int(input())
snail = [[0] * N for _ in range(N)]
direction = [[1, 0], [0, 1], [-1, 0], [0, -1]] # 하 우 상 좌
diCurrent = 0
cX = 0
cY = 0
findX = 0
findY = 0
nN = N * N

while True:
    if snail[cY][cX] == 0:
        snail[cY][cX] = nN
        nN -= 1
        if nN == 0:
            break
        cY += direction[diCurrent][0]
        cX += direction[diCurrent][1]

        if cY == N:
            cY -= 1
            diCurrent += 1
            if diCurrent == 4:
                diCurrent = 0
            cX += direction[diCurrent][1]

        if cY == -1:
            cY += 1
            diCurrent += 1
            if diCurrent == 4:
                diCurrent = 0
            cX += direction[diCurrent][1]

        if cX == N:
            cX -= 1
            diCurrent += 1
            if diCurrent == 4:
                diCurrent = 0
            cY += direction[diCurrent][0]

        if cX == -1:
            cX += 1
            diCurrent += 1
            if diCurrent == 4:
                diCurrent = 0
            cX += direction[diCurrent][1]

        if snail[cY][cX] != 0:
            cY -= direction[diCurrent][0]
            cX -= direction[diCurrent][1]
            diCurrent += 1
            if diCurrent >= 4:
                diCurrent = 0
            cY += direction[diCurrent][0]
            cX += direction[diCurrent][1]

for i in range(N):
    for j in range(N):
        if snail[i][j] == findNum:
            findX = i + 1
            findY = j + 1
        print(snail[i][j], end=" ")
    print()

print(findX, findY)