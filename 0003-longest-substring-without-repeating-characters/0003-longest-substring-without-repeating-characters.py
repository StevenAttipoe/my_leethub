class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0

        for i in range(len(s)):
            unique = set()

            for j in range(i, len(s)):
                if s[j] not in unique:
                    unique.add(s[j])
                else:
                    break

            maxLength = max(maxLength, len(unique))
        
        return maxLength
        