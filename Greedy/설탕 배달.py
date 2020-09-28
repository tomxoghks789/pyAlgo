def greedy(N):
    counter = 0
    while N > 0:
        if N % 5 == 0:
            N = N - 5
            counter += 1
        elif N % 3 == 0:
            N = N - 3
            counter += 1
        elif N - 5 > 0:
            N = N - 5
            counter += 1
        else:
            counter = -1
            break
    return counter

print(greedy(int(input())))