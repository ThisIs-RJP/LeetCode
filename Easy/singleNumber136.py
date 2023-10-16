#!/usr/bin/env python3

def single(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

### Testing
print(single([2,2,1]))
print(single([4,1,2,1,2]))
print(single([1]))
