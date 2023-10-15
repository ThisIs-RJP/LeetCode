#!/usr/bin/env python3

def div(dividend, divisor):
    if (2**31) <= int(dividend / divisor):
        return 2**31 - 1
    return int(dividend / divisor)
