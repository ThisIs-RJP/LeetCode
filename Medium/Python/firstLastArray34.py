def firstLast(nums, target):
    if target not in nums:
        return [-1, -1]
    indexs = [i for i in range(len(nums)) if nums[i] == target]
    return [indexs[0], indexs[-1]]
