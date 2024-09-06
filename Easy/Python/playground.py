#!/usr/bin/env python3

# print(str("{0:b}".format(5)))
print(int(str("{0:b}".format(5)).replace("0", ".").replace("1", "0").replace(".", "1"), 2))