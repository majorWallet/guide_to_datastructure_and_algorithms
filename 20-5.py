def sort_temp(ar): #hash table algorithm
    hash_table = {}
    i = 97.0
    while i <= 99.0:
        hash_table[round(i, 1)] = 0
        i += 0.1
    for i in ar:
        hash_table[i] += 1
    i = 0
    for key in hash_table.keys():
        j = 0
        while hash_table[key] > j:
            ar[i] = key
            i += 1
            j += 1
    return ar
print(sort_temp([98.6,98.0,97.1,99.0,98.9,97.8,98.5,98.2,98.0,97.1]))