def greedy(N):
    counter = [0, 0, 0]
    while N > 0:
        if N % 300 == 0:
            N = N - 300
            counter[0] += 1
        elif N % 60 == 0:
            N = N - 60
            counter[1] += 1
        elif N % 10 == 0:
            N = N - 10
            counter[2] += 1
        else:
            return -1
    return counter
ans = greedy(int(input()))
if ans == -1:
    print(ans)
else:
    for i in range(len(ans)):
        print(ans[i], end=" ")