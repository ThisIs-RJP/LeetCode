#!/usr/bin/env python3

def revInt(x):
    if x != 0 and (2**31) > int((abs(x) / x) * (int(str(x).strip("-")[::-1]))) and -(2**31) < int((abs(x) / x) * (int(str(x).strip("-")[::-1]))):
        return int((abs(x) / x) * (int(str(x).strip("-")[::-1])))
    else:
        return 0

###### TEST CASES

print(revInt(0))
print(revInt(1534236469))
print(revInt(123))
print(revInt(-123))
print(revInt(120))
