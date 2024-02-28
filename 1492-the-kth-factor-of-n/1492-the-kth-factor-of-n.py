class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        i = 1

        while len(factors) < k and i <= n:
            if n % i == 0:
                factors.append(i)

            i += 1

        return -1 if len(factors) != k else factors[-1]

        