#2810번
N = int(input())
S = input()
counter = 0
if S.count("S") == N:
    print(S.count("S"))
else:
    counter += S.count("LL")
    counter += S.count("S")
    print(counter + 1)