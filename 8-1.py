def intersection(arr1, arr2):
    hashArr = [False for i in range(10)]
    intersectionArr = []
    for i in arr1:
        hashArr[i] = True
    for i in arr2:
        if hashArr[i] == True:
            intersectionArr.append(i)
    return intersectionArr

print(intersection([1, 2, 3, 4, 5], [0, 2, 4, 6, 8]))