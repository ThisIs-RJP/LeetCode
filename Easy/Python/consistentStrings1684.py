#!/usr/bin/env python3

def countConsistentStrings(allowed, words):
    return sum([1 if set(word).issubset(set(allowed)) else 0 for word in words])

print(countConsistentStrings("ab", ["ad","bd","aaab","baa","badab"]))
print(countConsistentStrings("abc", ["a","b","c","ab","ac","bc","abc"]))
