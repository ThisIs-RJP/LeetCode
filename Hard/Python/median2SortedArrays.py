class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        both = sorted(nums1 + nums2)
        if len(both) % 2 != 0:
            return (both)[len(both) // 2]
        else:
            return ((both)[len(both) // 2 - 1] + (both)[len(both) // 2]) / 2
