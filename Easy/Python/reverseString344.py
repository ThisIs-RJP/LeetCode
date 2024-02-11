#!/usr/bin/env python3

s = ["h","e","l","l","o"]

def reversedString(s):
    word = "".join(s[::-1])
    for i in range(len(word)):
        s[i] = word[i]

reversedString(s)
