# 2941
def converter(str):
    dataList = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
    for i in range(8):
        str = str.replace(dataList[i], "0")
    return len(str)

print(converter(input()))