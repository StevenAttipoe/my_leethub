class Solution:
    def reverse(self, x: int) -> int:
        reversedNum = 0

        isNegative = x < 0

        if isNegative:
            x = abs(x)

        while x > 0:
            reversedNum = (reversedNum * 10) + (x % 10)
            x = x // 10

        if isNegative:
            reversedNum *= -1

        if ((reversedNum > 2 ** 31 - 1) or (reversedNum < -2 ** 31)):
            return 0

        return reversedNum

        