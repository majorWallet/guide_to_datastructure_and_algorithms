def reverse(array):
    for i in range(int(len(array)/2)):
        array[i], array[-i-1] = array[-i-1], array[i]
    return array
print(reverse([1,2,3,4,5]))