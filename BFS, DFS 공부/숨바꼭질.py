# 1697
from collections import deque

LIMIT = 100001

N, K = map(int, input().split())

def find():
    counter = 0
    que = deque([N])
    qc = deque([0])

    while que:
        temp = que.popleft()
        counter = qc.popleft()

        if temp == K:
            break

        for nx in (temp+1, temp-1, temp*2):
            if 0 <= nx < LIMIT and not mapData[nx]:
                que.append(nx)
                qc.append(counter + 1)
                mapData[nx] = 1
    return counter

mapData = [0] * LIMIT
print(find())