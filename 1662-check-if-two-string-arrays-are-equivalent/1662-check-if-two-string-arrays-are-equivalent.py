class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        string1 = []
        string2 = []

        for w in word1:
            string1.append(w)

        for w in word2:
            string2.append(w)

        return ''.join(string1) == ''.join(string2)

        