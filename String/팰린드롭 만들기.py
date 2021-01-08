# 1213

def palindrome(str):
    oddCount = 0
    oddChar = ''
    strAns = ''
    ans = [0] * 26

    for i in str:
        ans[ord(i)  - 65] += 1

    for i in range(26):
        if ans[i] % 2 == 1:
            oddCount += 1
            oddChar = chr(i + 65)
            if oddCount >= 2:
                return "I'm Sorry Hansoo"
        strAns += chr(i + 65) * (ans[i] // 2)
    return strAns + oddChar + strAns[::-1]

print(palindrome(input()))