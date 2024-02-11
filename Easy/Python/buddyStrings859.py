class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        m = []

        for i in range(len(s)):
            if s[i] != goal[i]:
                m.append((s[i], goal[i]))
        
        if len(m) == 2 and m[0] == m[1][::-1]:
            return True
        
        if len(m) == 0 and len(set(s)) < len(s):
            return True
        
        return False
