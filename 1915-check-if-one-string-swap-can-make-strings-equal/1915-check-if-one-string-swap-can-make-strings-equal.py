class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        swaps = 0

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                swaps += 1

        return s1 == s2 or sorted(s1) == sorted(s2) and swaps == 2