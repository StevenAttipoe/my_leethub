class Solution:
    # def longestPalindrome(self, s: str) -> str:
        
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        l = r = 0
        n = len(s)
        for i in range(n):
            for j in range(i, n):
                if s[i] == s[j]:
                    substr = s[i:j+1]
                    if substr == substr[::-1] and len(substr) > r - l + 1:
                        l = i
                        r = j

        return s[l : r + 1]
                        
                    
        