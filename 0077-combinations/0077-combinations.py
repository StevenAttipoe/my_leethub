class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        comb = [0] * k
        i = 0

        while i >= 0:
            comb[i] += 1

            if comb[i] > n:
                i -= 1
            elif i == k - 1:
                result.append(comb[:])
            else:
                i += 1
                comb[i] = comb[i - 1]

        return result
            




        