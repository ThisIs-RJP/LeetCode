#!/usr/bin/env python3

def reversePrefix(word, ch):
    return (word[:word.index(ch) + 1])[::-1] + "" + (word[word.index(ch) + 1::])

print(reversePrefix("abcdefd", "d"))