class Solution:
    def minFlips(self, target: str) -> int:
        minNoOfFlips = 0
        prev = '0'
        for c in target:
            if prev != c:
                minNoOfFlips += 1
            prev = c
        return minNoOfFlips