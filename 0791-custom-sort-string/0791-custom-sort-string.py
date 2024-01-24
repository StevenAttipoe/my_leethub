class Solution:
    def customSortString(self, order: str, s: str) -> str:
        rank = [26] * 26

        for i, char in enumerate(order):
            unicodeIndex = ord(char) - ord('a')
            rank[unicodeIndex] = i

        stringArray = list(s)
        stringArray.sort(key = lambda c: rank[ord(c) - ord('a')])        

        return ''.join(stringArray)

        