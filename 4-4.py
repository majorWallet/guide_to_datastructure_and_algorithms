#O(N^2)
"""
def greatestNumber(array):
    for i in array:
        isIValTheGreatest = True

        for j in array:
            if j > i:
                isIValTheGreatest = False

        if isIValTheGreatest:
            return i
"""
#O(N)
def greatestNumber(array):
    max = array[0]
    for i in array:
        if max < i:
            max = i
    return max