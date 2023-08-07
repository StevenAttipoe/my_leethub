class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result  = []

        a = list(a)
        b = list(b)

        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())

            result.append(str(carry % 2))
            carry //= 2

        return ''.join(result)[::-1]
