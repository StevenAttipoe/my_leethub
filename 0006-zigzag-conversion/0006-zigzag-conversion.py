class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        zigzagRows = [""] * numRows
        isGoingUp = True
        i = 0

        for char in s:
            zigzagRows[i] += char

            if i == numRows - 1:
                isGoingUp = False
            elif i == 0:
                isGoingUp = True

            if isGoingUp:
                i += 1
            else:
                i -= 1

        return "".join(zigzagRows)
