class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return
        min_len = min(len(s) for s in strs)
        result = ""
        for i in range(min_len):
            char = strs[0][i]
            if all(s[i] == strs[0][i] for s in strs):
                result += strs[0][i]
            else:
                break
        return result
