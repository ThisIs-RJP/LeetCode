#!/usr/bin/env python3

def isomorphic(s, t):
    # dict1 = {}
    # dict2 = {}
    # sD = ""
    # tD = ""

    # if len(s) == len(t):
    #     for i in range(len(s)):
    #         if s[i] not in dict1 or t[i] not in dict2:
    #             dict1[s[i]] = str(i) + "."
    #             dict2[t[i]] = str(i) + "."
    # else:
    #     return False
    # for i in range(len(s)):
    #     sD = sD + dict1[s[i]]
    #     tD = tD + dict2[t[i]]
    # return sD == tD
    """
        Everything above is the old code,
        it was super slow, so below will be the updated version
    """
    if len(s) != len(t):
        return False

    dict1 = {}
    dict2 = {}

    for i in range(len(s)):
        if (s[i] in dict1 and dict1[s[i]] != t[i]) or (t[i] in dict2 and dict2[t[i]] != s[i]):
            return False
        dict1[s[i]] = t[i]
        dict2[t[i]] = s[i]
    

    return True
