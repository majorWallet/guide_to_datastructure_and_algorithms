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

arr = [0, 5, 2, 1, 6, 3]
sorted_Arr = QuickSort(arr)
sorted_Arr.quick_sort(0, len(arr)-1)
print(sorted_Arr.get_arr())