# 12761

from collections import deque
LIMIT = 100001
visted = [0] * LIMIT

A, B, N, M = map(int, input().split())

que = deque()
que.append([N, 0])
ans = 0
while que:
    cx, cc = que.popleft()
    if cx == M:
        ans = cc
        break
    if visted[cx] == 1:
        continue
    visted[cx] = 1
    for val in [cx + 1, cx - 1, cx + A, cx + B, cx - A, cx - B, cx * A, cx * B, cx - (cx * A), cx - (cx * B)]:
        if -1 < val < LIMIT and not visted[val]:
            que.append([val, cc + 1])
print(ans)