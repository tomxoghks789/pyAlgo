# 140916
def greedy(N):
    ans = 0
    while True:
        if N == 0:
            return ans
        if N < 0:
            return -1
        t1 = N % 5
        if t1 == 0:
            ans += N // 5
            return ans
        else:
            N = N - 2
            ans += 1
print(greedy(int(input())))