def recursive_count(arr):
    if not arr:
        return 0
    else:
        return recursive_count(arr[1:]) + 1


print(recursive_count([1, 2, 3, 4]))
