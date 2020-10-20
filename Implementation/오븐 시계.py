hour, minTime = map(int, input().split())
minute = int(input())

minTime += minute
if minTime >= 60:
    x, y = divmod(minTime, 60)
    hour += x
    minTime = y
    if hour >= 24:
        hour -= 24
print(hour, minTime)