class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            char = s[i]
            isUnique = True
            for j in range(len(s)):
                if i != j and char == s[j]:
                    isUnique = False
                    break
            if isUnique:
                return i
        return -1

        