class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        paddedString = "".join((s[1:], s[:-1]))
        return s in paddedString