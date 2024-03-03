class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        maxLength = 0

        forbiddenSet = set(forbidden)
        r = len(word) - 1

        for l in range(len(word) -1, -1, -1):
            for i in range(l, min(l + 10, r + 1)):
                if word[l:i + 1] in forbiddenSet:
                    r = i - 1
                    break

            maxLength = max(maxLength, r - l + 1)

        return maxLength
            