class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        s = [(sum(row), i) for i, row in enumerate(mat)]
        s.sort()
        w = [soldier[1] for soldier in s[:k]]
        return w
