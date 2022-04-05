def recursive_max(nums):
    if not nums:
        return None
    elif len(nums) == 1:
        return nums[0]
    else:
        sub_max = recursive_max(nums[1:])
        return nums[0] if nums[0] > sub_max else sub_max


print(recursive_max([5, 2, -3, 4]))
