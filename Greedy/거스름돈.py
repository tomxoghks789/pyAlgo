def greedy(N):
    counter = 0
    while N > 0:
        if N % 500 == 0:
            N = N - 500
            counter += 1
        elif N % 100 == 0:
            N = N - 100
            counter += 1
        elif N % 50 == 0:
            N = N - 50
            counter += 1
        elif N % 10 == 0:
            N = N - 10
            counter += 1
        elif N % 5 == 0:
            N = N - 5
            counter += 1
        else:
            N = N - 1
            counter += 1
    return counter
print(greedy(1000 - int(input())))
