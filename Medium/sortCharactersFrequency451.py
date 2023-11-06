class Solution:
    def frequencySort(self, s: str) -> str:
        i = {}
        newWord = ""

        for c in s:
            if c not in i:
                i[c] = 1
            elif c in i:
                i[c] = i[c] + 1
            
        iNew = dict(sorted(sorted(i.items()), key=lambda item: item[1], reverse=True))
        for k, v in iNew.items():
            newWord = newWord + (k * v)
        
        return newWord
