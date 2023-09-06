class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9

    def addDigits2(self, num: int) -> int:
        def helper(num):
            if num < 10:
                return num

            digits = []
            while num:
                digit = num % 10
                num = num // 10
                digits.append(digit)

            return helper(sum(digits))

        return helper(num)

                