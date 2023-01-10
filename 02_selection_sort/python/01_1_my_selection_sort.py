def find_smallest(arr):
    smallest_idx = 0
    smallest = arr[smallest_idx]
    for i in range(1, len(arr)):
        el = arr[i]
        if el <= smallest:
            smallest_idx = i
            smallest = el
    return smallest_idx


def selection_sort(arr):
    sorted_arr = []
    for i in range(len(arr)):
        smallest_idx = find_smallest(arr)
        smallest = arr.pop(smallest_idx)
        sorted_arr.append(smallest)
    return sorted_arr


print(selection_sort([5, 3, 6, 2, 10]))
