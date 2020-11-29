# 5597

ansList = [0] * 31

for i in range(28):
    ansList[int(input())] = 1

for i in range(1, 31):
    if ansList[i] == 0:
        print(i)