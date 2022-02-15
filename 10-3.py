def sum(low, high):
    if high == low:
        return high
    else:
        return high + sum(low, high-1)
print(sum(2, 11))