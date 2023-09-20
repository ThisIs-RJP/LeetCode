def sortColors(nums) :
    for a in range(len(nums)):
        print(nums)
        for b in range(len(nums) - a - 1):
            if nums[b] > nums[b + 1]:
                temp = nums[b]
                nums[b] = nums[b+1]
                nums[b+1] = temp
            print(nums)
