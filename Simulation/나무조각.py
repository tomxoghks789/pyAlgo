# 2947

def printList(L):
    for i in range(len(L)):
        print(L[i], end=" ")
    print()

inputList = list(map(int, input().split()))
sortedList = sorted(inputList)

while inputList != sortedList:
    for i in range(len(inputList) - 1):
        if inputList[i] > inputList[i + 1]:
            temp = inputList[i + 1]
            inputList[i + 1] = inputList[i]
            inputList[i] = temp
            printList(inputList)