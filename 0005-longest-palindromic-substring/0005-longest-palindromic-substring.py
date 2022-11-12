class Solution:
    def longestPalindrome(self, s: str) -> str:
        lps = ""
        lpsLen = 0
        for i in range(len(s)):
            #Odd length
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if lpsLen < r - l + 1:
                    lps = s[l:r + 1]
                    lpsLen = r-l + 1
                l -= 1
                r += 1
                            
            #Even length 
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if lpsLen < r - l + 1:
                    lps = s[l:r + 1]
                    lpsLen = r-l + 1
                l -= 1
                r += 1
        return lps
            
        