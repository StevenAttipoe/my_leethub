class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charFreq1 = [0] * 26
        charFreq2 = [0] * 26

        for char in s:
            charFreq1[ord(char) - ord('a')] += 1
        
        for char in t:
            charFreq2[ord(char) - ord('a')] += 1
        
        return charFreq1 == charFreq2
        