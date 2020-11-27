# 2812
import sys

length, delete = map(int, sys.stdin.readline().strip().split())
valNum = list(sys.stdin.readline().strip())
ans = [valNum[0]]

for i in range(1, length):
    if len(ans) == length - delete:
        if i != length and delete == 0:
            ans.append(valNum[i:])
        break
    while len(ans) > 0 and ans[-1] < valNum[i] and delete > 0:
        ans.pop()
        delete -= 1
    ans.append(valNum[i])

print(''.join(ans))