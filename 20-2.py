def find_missing_num(ar): #pattern algorithm
    return sum(range(len(ar) + 1)) - sum(ar)

print(find_missing_num([2,3,0,6,1,5]))