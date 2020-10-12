# 1번
def solu(N):
    ans = [0, 0]
    for i in range(2, 10):
        tN = N
        result = 1
        while tN != 0:
            result *= tN % i
            tN //= i
        if ans[1] <= result:
            ans = [i, result]
    return ans
print(solu(10))
