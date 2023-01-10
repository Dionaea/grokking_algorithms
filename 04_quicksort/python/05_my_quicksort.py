def quicksort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    mid_el = arr[mid]
    less = []
    greater = []
    for el in arr[:mid] + arr[mid + 1:]:
        if el > mid_el:
            greater.append(el)
        else:
            less.append(el)

    return quicksort(less) + [arr[mid]] + quicksort(greater)


print(quicksort([10, 5, 2, 3]))
