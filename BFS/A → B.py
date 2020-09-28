from queue import Queue

LIMIT = 1000000001

def BFS():
    flag = 0
    counter = 1
    que = Queue()
    que.put([A, counter])
    while not que.empty():
        tx, tc = que.get()
        counter = tc
        if tx == B:
            flag = 1
            break
        for nx in (tx * 2, int(str(tx)+'1')):
            if 0 < nx < LIMIT:
                que.put([nx, tc + 1])
    if flag:
        return counter
    return -1

A, B = map(int, input().split())

print(BFS())