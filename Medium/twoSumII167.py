#!/usr/bin/env python3

def twoSum(numbers, target):
    numDict = {}
    for i, num in enumerate(numbers):
        if target - num in numDict:
            return [numDict[target - num] + 1, i + 1]
        numDict[num] = i
