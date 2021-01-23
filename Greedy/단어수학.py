# 1339

ans = 0
value = 9
alphabet = [0] * 26

for i in range(int(input())):
    bias = 0
    for j in input()[::-1]:
        alphabet[ord(j) - 65] += 10 ** bias
        bias += 1

alphabet.sort(reverse=True)

for i in range(26):
    if alphabet[i] == 0:
        break
    ans += value * alphabet[i]
    value -= 1
print(ans)