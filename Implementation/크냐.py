import sys
while 1:
    x, y = map(int, sys.stdin.readline().split())
    if x == y == 0:
        break
    if x > y:
        print("Yes")
    else:
        print("No")