from queue import Queue

que = Queue()
que.put([9, 4])
while not que.empty():
    x, y = que.get()
    print(x, y)
    que.put([4, 6])


