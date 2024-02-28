class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        kFactor = 1
        factorCount = 0
        i = 1

        while factorCount < k and i <= n:
            if n % i == 0:
                kFactor = i
                factorCount += 1

            i += 1

        return -1 if factorCount != k else kFactor

    def kthFactor2(self, n: int, k: int) -> int:
        factors = []
        i = 1

        while len(factors) < k and i <= n:
            if n % i == 0:
                factors.append(i)

            i += 1

        return -1 if len(factors) != k else factors[-1]

        