N = int(input())
txt = input()
A = 0
B = 0
for i in range(len(txt)):
    if txt[i] == "A":
        A +=1
    else:
        B +=1
if A > B :
    print("A")
elif B > A:
    print("B")
else:
    print("Tie")