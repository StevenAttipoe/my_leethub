class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        i = j = 0
        p1 = p2 = 0

        while i < len(word1) and j < len(word2):
            if word1[i][p1] != word2[j][p2]:
                return False   

            p1 += 1
            p2 += 1

            if p1 >= len(word1[i]):
                i += 1
                p1 = 0

            if p2 >= len(word2[j]):
                j += 1
                p2 = 0                

        return i == len(word1) and j == len(word2)


    def arrayStringsAreEqual2(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)

        