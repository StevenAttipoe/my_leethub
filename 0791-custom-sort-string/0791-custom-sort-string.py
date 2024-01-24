class Solution:
    # O(n) runtime & O(n) space
    def customSortString(self, order: str, s: str) -> str:
        charFreq = Counter(s)
        res = []

        for char in order:
            if char in charFreq:
                res.append(char * charFreq[char])
                charFreq[char] = 0

        for char, freq in charFreq.items():
            res.append(char * freq)
        
        return ''.join(res)


    # O(nlogn) runtime & O(n) space
    def customSortString2(self, order: str, s: str) -> str:
        rank = [26] * 26

        for i, char in enumerate(order):
            unicodeIndex = ord(char) - ord('a')
            rank[unicodeIndex] = i

        stringArray = list(s)
        stringArray.sort(key = lambda c: rank[ord(c) - ord('a')])        

        return ''.join(stringArray)

        