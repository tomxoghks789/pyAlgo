# 12851

from collections import deque

def find(N):
    que = deque()
    que.append(N)
    mapData[N][0] = 0
    mapData[N][1] = 1
    while que:
        temp = que.popleft()
        for nx in (temp + 1, temp - 1, temp * 2):
            if 0 <= nx < LIMIT :
                if mapData[nx][0] == -1:
                    mapData[nx][0] = mapData[temp][0] + 1
                    mapData[nx][1] = mapData[temp][1]
                    que.append(nx)
                elif mapData[nx][0] == mapData[temp][0] + 1:
                    mapData[nx][1] += mapData[temp][1]

LIMIT = 100001
N, K = map(int, input().split())
mapData = [[-1, 0] for _ in range(LIMIT)] # 값, 방법, 출현 수
find(N)
print(mapData[K][0])
print(mapData[K][1])