#!/usr/bin/env python3

def missingNumber(nums):
    return ((len(nums) * (len(nums) + 1)) // 2) - sum(nums)
