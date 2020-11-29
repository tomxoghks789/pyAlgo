# 10989
f = open(0)
f.readline()

LIMIT = 10001
data = [0] * LIMIT

for i in f:
    data[int(i)] += 1
for i in range(LIMIT):
    dataVal = data[i]
    if dataVal != 0:
        for j in range(dataVal):
            print(i)