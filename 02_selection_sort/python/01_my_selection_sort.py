def find_smallest(nums):
    min_num = nums[0]
    min_idx = 0
    for i, num in enumerate(nums):
        if num < min_num:
            min_num = num
            min_idx = i
    return min_num, min_idx


def selection_sort(nums):
    nums_sorted = []
    while nums:
        min_num, min_idx = find_smallest(nums)
        del nums[min_idx]
        nums_sorted.append(min_num)
    return nums_sorted


print(selection_sort([5, 3, 6, 2, 10]))
