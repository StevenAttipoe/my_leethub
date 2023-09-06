class Solution:
    def addDigits(self, num: int) -> int:
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

                