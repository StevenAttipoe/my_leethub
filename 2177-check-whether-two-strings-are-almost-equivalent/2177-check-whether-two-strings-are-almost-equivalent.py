class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        count1 = Counter(word1)
        count2 = Counter(word2)

        for i in range(26):
            char = chr(i + ord('a'))
            diff = abs(count1[char] - count2[char])
            if diff > 3:
                return False

        return True


        