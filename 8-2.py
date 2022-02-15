def findDuplicate(arr):
    hashTable = {}
    for i in arr:
        hashTable[i] = False
    for i in arr:
        if not hashTable[i]:
            hashTable[i] = True
        else:
            return i
    return "null"

print(findDuplicate(['a', 'b', 'c', 'd', 'e', 'f', 'b', 'a', 'b']))