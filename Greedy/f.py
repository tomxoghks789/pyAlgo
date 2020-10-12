from datetime import datetime, timedelta

temp = ["02/28 23:59:00 03","03/01 00:00:00 02", "03/01 00:05:00 01"] #2
# ["10/01 23:20:25 30", "10/01 23:25:50 26", "10/01 23:31:00 05", "10/01 23:33:17 24", "10/01 23:50:25 13", "10/01 23:55:45 20", "10/01 23:59:39 03", "10/02 00:10:00 10"]	4
def go(n, customers):
    current = 0
    ans = []
    ans.append([0] * n)
    ans.append([datetime(1900,1,1)] * n)
    for i in range(len(customers)):
        timeData = customers[i].split(" ")
        tempTime = datetime.strptime(timeData[0] + timeData[1], '%m/%d%H:%M:%S')

        for j in range(n):
                if ans[1][current] + timedelta(minutes=int(timeData[2])) > tempTime:
                    ans[1][current] = tempTime + timedelta(minutes=int(timeData[2]))
                    if ans[0][current] == 0:
                        ans[0][current] = 1
                    else:
                        ans[0][current] += 1
                    current +=1
                    if current >= n:
                        current =0
        print(ans)
    return max(ans[0])

print(go(2, temp))