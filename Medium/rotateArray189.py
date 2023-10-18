#!/usr/bin/env python3

def rotate(nums, k):
        k = k % len(nums) 
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
