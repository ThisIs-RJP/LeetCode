class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def again(cp):
            if len(cp) == len(nums):
                p.append(cp[:])
                return
            for num in nums:
                if num not in cp:
                    cp.append(num)
                    again(cp)
                    cp.pop()

        p = []
        again([])
        return p
