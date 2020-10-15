import sys

def greedy(T):
    counter = 1
    tempVal = T[0][1]
    for i in range(1, N):
        if T[i][0] >= tempVal:
            tempVal = T[i][1]
            counter += 1
    return counter

N = int(sys.stdin.readline())
T = []
for i in range(N):
    T.append(list(map(int, sys.stdin.readline().split())))

T.sort(key= lambda x: (x[1], x[0]))

print(greedy(T))