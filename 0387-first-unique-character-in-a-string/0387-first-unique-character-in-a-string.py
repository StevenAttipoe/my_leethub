class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}

        for char in s:
            freq[char] = freq.get(char, 0) + 1

        for i, char in enumerate(s):
            if freq[char] == 1:
                return i
        return -1

    def firstUniqChar2(self, s: str) -> int:
        for i in range(len(s)):
            for j in range(len(s)):
                if i != j and s[i] == s[j]:
                    break
            else:
                return i

        return -1

        

        