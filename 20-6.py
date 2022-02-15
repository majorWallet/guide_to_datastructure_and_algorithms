def longest_consecutive_sequence(ar): #hash table algorithm
    hash_table = {}
    arr = []
    for i in range(min(ar), max(ar)+1):
        hash_table[i] = False
    for i in ar:
        hash_table[i] = True
    for key in hash_table.keys():
        if hash_table[key] == True:
            arr.append(key)
    return arr
print(longest_consecutive_sequence([10,5,12,3,55,30,4,11,2]))