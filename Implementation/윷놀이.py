# 2490
import sys
ans = []
for _ in range(3):
    count = list(map(int, sys.stdin.readline().split())).count(1)
    if count == 4:
        ans.append("E")
    elif count == 3:
        ans.append("A")
    elif count == 2:
        ans.append("B")
    elif count == 1:
        ans.append("C")
    else:
        ans.append("D")
for i in range(3):
    print(ans[i])