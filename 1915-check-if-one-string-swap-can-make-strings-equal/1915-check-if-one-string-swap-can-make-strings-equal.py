class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        swaps = 0

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                swaps += 1

        return Counter(s1) == Counter(s2) and (swaps == 0 or swaps == 2)