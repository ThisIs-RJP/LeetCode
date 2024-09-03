#!/usr/bin/env python3

import math

def getLucky(s, k):

    s = s.lower()
    # alphabet = {chr(i+96):f"({i})" for i in range(1,27)} ### Would've been nice...
    alphabet = {'a': '(1)', 'b': '(2)', 'c': '(3)', 'd': '(4)', 'e': '(5)', 'f': '(6)', 'g': '(7)', 'h': '(8)', 'i': '(9)', 'j': '(10)', 'k': '(11)', 'l': '(12)', 'm': '(13)', 'n': '(14)', 'o': '(15)', 'p': '(16)', 'q': '(17)', 'r': '(18)', 's': '(19)', 't': '(20)', 'u': '(21)', 'v': '(22)', 'w': '(23)', 'x': '(24)', 'y': '(25)', 'z': '(26)'}

    for letter in alphabet.keys():
        s = s.replace(letter, alphabet[letter])

    s = int("".join(s[1:-1].split(")(")))
    k = k - 1

    if k > 0:
        for i in range(k + 1):
            if k > 0:
                s = sum([int(d) for d in str(s)])

            else:
                s = sum(eval(i) for i in s)
        
        return s
    
    else:
        return sum([int(d) for d in str(s)])

print(getLucky("ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss", 2))
print(getLucky("leetcode", 2))
