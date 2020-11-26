# 10808

stringData = input()

alphabet = [0] * 26
for i in range(len(stringData)):
    alphabet[ord(stringData[i]) - 97] += 1
for i in range(len(alphabet)):
    print(alphabet[i], end=" ")