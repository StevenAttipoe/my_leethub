class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        count = [0] * 26

        for i in range(len(word1)):
            count[ord(word1[i]) - ord('a')] += 1
            count[ord(word2[i]) - ord('a')] -= 1

        for i in range(26):
            if abs(count[i]) > 3:
                return False

        return True

    def checkAlmostEquivalent2(self, word1: str, word2: str) -> bool:
        count1 = Counter(word1)
        count2 = Counter(word2)

        for i in range(26):
            char = chr(i + ord('a'))
            diff = abs(count1[char] - count2[char])
            if diff > 3:
                return False

        return True


        