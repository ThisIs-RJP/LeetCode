#!/usr/bin/env python3

s = "hello"
s2 = "leetcode"
s3 = "aA"
vowels = "aeiou"

def reverseV(s):
    s = [c for c in s]
    v = [c for c in s if c.lower() in vowels][::-1]
    k = 0
    for i in range(len(s)):
        if s[i].lower() in vowels:
            s[i] = v[k]
            k = k + 1
    return("".join(s))

print(reverseV(s))
print(reverseV(s2))
print(reverseV(s3))
