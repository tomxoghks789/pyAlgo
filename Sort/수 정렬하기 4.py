# 11931

import sys
data = []
dataLen = int(sys.stdin.readline())

for i in range(dataLen):
    data.append(int(sys.stdin.readline()))

for i in sorted(data, reverse=True):
    print(i)