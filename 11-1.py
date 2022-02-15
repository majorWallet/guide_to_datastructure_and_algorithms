def cntStr(arr):
    if len(arr) == 0:
        return 0
    else:
        return cntStr(arr[1:]) + len(arr[0])

print(cntStr(["ab", "c", "def", "ghij"]))