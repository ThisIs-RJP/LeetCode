#!/usr/bin/env python3

def p(row):
    output = [[1], [1,1]]
    if row == 1 or row == 2:
        return [[1]] if row == 1 else output

    for i in range(row - 2):
        last = output[-1]
        output.append([last[0]] + [(last[i] + last[i + 1]) for i in range(len(last) - 1)] + [last[-1]])
    return output
