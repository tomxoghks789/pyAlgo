# 3059

for i in range(int(input())):
    alpha = [1] * 26
    ans = 0
    txt = input()
    for j in txt:
        alpha[ord(j) - 65] = 0
    for num, txt in enumerate(alpha):
        if txt == 1:
            ans += num + 65
    print(ans)