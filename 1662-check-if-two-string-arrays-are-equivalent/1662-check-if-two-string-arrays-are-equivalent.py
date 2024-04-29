class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        i = j = 0
        p1 = p2 = 0

        while i < len(word1) and j < len(word2):
            while p1 < len(word1[i]) or p2 < len(word2[j]):
                if word1[i][p1] != word[j][p2]:
                    break

                p1 += 1
                p2 += 1

            if p1 >= len(word1[i]):
                i += 1
            elif p2 >= len(word2[j]):
                j += 1
            else:
                return False

        return True


    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)

        