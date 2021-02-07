# 1764
import sys
n, m = map(int, input().split())
aList = set()
bList = set()
for i in range(n):
    aList.add(sys.stdin.readline().strip())
for i in range(m):
    bList.add(sys.stdin.readline().strip())

ans = sorted(list(aList & bList))
print(len(ans))
for i in ans:
    print(i)
