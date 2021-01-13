# SW Expert 2567
for test_case in range(1, int(input()) + 1):
    inputData = int(input())
    ans = "No"
    if inputData % 10 == 9 or inputData // 10 == 9:
        ans = "Yes"
    print("#" + str(test_case), ans)