# 10250

T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())
    X, Y = divmod(N, H)
    if Y == 0:
        Y = H
        print(Y * 100+ X)
    else:
        X += 1
        print(Y*100+X)