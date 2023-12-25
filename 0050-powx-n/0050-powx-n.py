class Solution:
    # O(logn)
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            x = 1 / x
            n = abs(n)

        if n % 2 == 0:
            return self.myPow(x * x, n // 2)
        else:
            return x * self.myPow(x * x, n // 2)

    # O(n)
    def myPow2(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            x = 1 / x
            n = abs(n)

        res = 1
        while n > 0:
            res *= x
            n -= 1

        return res
