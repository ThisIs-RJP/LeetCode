def longestSS(s):
    x = set()
    maxLength = 0
    l, r = 0, 0

    while r < len(s):
        if s[r] not in x:
            x.add(s[r])
            r += 1
            maxLength = max(maxLength, r - l)
        else:
            x.remove(s[l])
            l += 1

    return maxLength
