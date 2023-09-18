class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        charSum = 0
        for char in t:
            charSum += ord(char)

        for char in s:
            charSum -= ord(char)

        return chr(charSum)


    def findTheDifference2(self, s: str, t: str) -> str:
        for char in t:
            if t.count(char) != s.count(char):
                return char
            
        