def recursive_sum(nums):
    if len(nums) == 0:
        return 0
    return nums[0] + recursive_sum(nums[1:])


print(recursive_sum([1, 2, 3, 4]))
