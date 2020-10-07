# 11047번  동전 0

N, K = map(int, input().split())
counter = 0
A = []

for _ in range(N):
    temp = int(input())
    if temp <= K:
        A.append(temp)

A.reverse()

for i in A:
    x = K // i
    K -= x * i
    counter += x

print(counter)