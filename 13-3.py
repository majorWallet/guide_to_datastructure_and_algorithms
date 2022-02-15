class QuickSort:
    def __init__(self, array):
        self.array = array
    
    def partition(self, left_pointer, right_pointer):
        pivot_pointer = right_pointer
        pivot_val = self.array[pivot_pointer]
        right_pointer -= 1

        while True:
            while self.array[left_pointer] < pivot_val:
                left_pointer += 1
            while self.array[right_pointer] > pivot_val:
                right_pointer -= 1

            if left_pointer >= right_pointer:
                break
        
            else:
                self.array[left_pointer], self.array[right_pointer] = self.array[right_pointer], self.array[left_pointer]
                left_pointer += 1

        self.array[left_pointer], self.array[pivot_pointer] = self.array[pivot_pointer], self.array[left_pointer]

        return left_pointer

    def quick_sort(self, left_pointer, right_pointer):
        if left_pointer >= right_pointer:
            return None
        
        pivot_pointer = self.partition(left_pointer, right_pointer)
        self.quick_sort(left_pointer, pivot_pointer - 1)
        self.quick_sort(pivot_pointer + 1, right_pointer)

    def get_arr(self):
        return self.array


def find_biggest_num_1(arr):
    for i in arr:
        iIsGreatestNum = True
        for j in arr:
            if i < j:
                iIsGreatestNum = False
        if iIsGreatestNum:
            return i

def find_biggest_num_2(arr):
    sortedArr = QuickSort(arr)
    sortedArr.quick_sort(0, len(arr)-1)
    sortedArr = sortedArr.get_arr()
    return sortedArr[-1]

def find_biggest_num_3(arr):
    max = arr[0]
    for i in arr:
        if max < i:
            max = i
    return max

arr = [0, 5, 2, 1, 6, 3]
print(find_biggest_num_1(arr))
print(find_biggest_num_2(arr))
print(find_biggest_num_3(arr))