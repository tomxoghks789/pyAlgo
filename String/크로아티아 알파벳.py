# 2941
def converter(str):
    dataList = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
    for i in range(len(str)):
        if i >= len(str):
            break
        for j in range(8):
            if str[i] in dataList[j]:
                str = str.replace(dataList[j], "0", 1)
    return len(str)

print(converter(input()))