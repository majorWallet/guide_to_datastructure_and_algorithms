def printLowHigh(low, high):
    if low > high:
        return None
    else:
        print(low)
        printLowHigh(low + 2, high)

printLowHigh(1, 11)