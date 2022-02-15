def findNotDuplicate(str):
    hashTable = {}
    for i in str:
        hashTable[i] = 0
    for i in str:
        hashTable[i] += 1
    for i in str:
        if hashTable[i] == 1:
            return i
print(findNotDuplicate("minimum"))