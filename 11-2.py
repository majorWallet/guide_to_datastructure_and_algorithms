def return_only_even(arr):
    if len(arr) == 0:
        return []
    else:
        if arr[0] % 2 == 0:
            return return_only_even(arr[1:]) + [arr[0]]
        else:
            return return_only_even(arr[1:])

print(return_only_even([1, 2, 4]))