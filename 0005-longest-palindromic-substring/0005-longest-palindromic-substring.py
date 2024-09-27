class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        result = ""
        n = len(s)
        for i in range(n):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    substr = s[i:j+1]
                    if substr == substr[::-1] and len(substr) > len(result):
                        result = substr
        

        return result
                        
                    
        