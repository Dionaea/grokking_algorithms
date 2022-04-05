def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        foundation = arr.pop()
        less = [el for el in arr if el < foundation]
        bigger = [el for el in arr if el >= foundation]
        return quicksort(less) + [foundation, ] + quicksort(bigger)


print(quicksort([10, 5, 2, 3]))
