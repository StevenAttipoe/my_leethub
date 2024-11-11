class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        l = 0
        unique = set()

        for r in range(len(s)):
            if s[r] not in unique:
                unique.add(s[r])
            else:
                while l <= r and s[r] in unique:
                    unique.remove(s[l])
                    l += 1
                unique.add(s[r])
                    
            maxLength = max(maxLength, len(unique))
        
        return maxLength


    def lengthOfLongestSubstring2(self, s: str) -> int:
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
        