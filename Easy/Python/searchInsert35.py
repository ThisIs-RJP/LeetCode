#!/usr/bin/env python3

def search(nums, target):
    if target in nums:
        return nums.index(target)
    else:
        return sorted((nums + [target])).index(target)
