# 1697
from collections import deque
N, K = map(int, input().split())
visited = []

def find():
    counter = 0
    que = deque([N])
    qc = deque([0])
    visited.append(N)

    while que:
        temp = que.popleft()
        c = qc.popleft()
        counter = c

        if temp == K:
            break

        for nx in (temp+1, temp-1, temp*2):
            if N <= nx < K:
                if nx not in visited:
                    que.append(nx)
                    visited.append(nx)
                    qc.append(c + 1)

    return counter

mapData = list(range(N, K+1))
print(find())