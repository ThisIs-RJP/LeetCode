class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        output = [[1], [1,1]]
        if rowIndex == 0:
            return [1] if rowIndex == 0 else output

        for i in range(rowIndex - 2 + 1):
            last = output[-1]
            # output.append([last[0]] + [(last[j] + last[j + 1]) for j in range(len(last) - 1)] + [last[-1]])
            output.append([1] + [(last[j] + last[j + 1]) for j in range(len(last) - 1)] + [1])
        return output[-1]
