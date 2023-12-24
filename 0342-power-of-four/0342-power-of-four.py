class Solution:
    # n = 4^x
    # log n = log 4^x
    # log n = xlog 4
    # log4 n = x log4 4
    # log4 n = x
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        return log(n, 4) % 1 == 0

    def isPowerOfFour2(self, n: int) -> bool:
        if n == 1:
            return True

        x = 1
        while x < n:
            x *= 4
        
        if x == n:
            return True
        return False

    def isPowerOfFour3(self, n: int) -> bool:
        if n == 1:
            return True
        if n <= 0 or n % 4 != 0:
            return False
        
        return self.isPowerOfFour(n // 4) 