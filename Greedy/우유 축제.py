# 14720번
N = int(input())
S = list(map(int, input().split()))
counter = 0
current = 0
for i in range(len(S)):
    if S[i] == current:
        counter += 1
        current += 1
        if current == 3:
            current = 0
print(counter)