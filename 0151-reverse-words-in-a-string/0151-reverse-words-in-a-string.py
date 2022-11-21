class Solution:
    def reverseWords(self, s: str) -> str:
        res = ''
        l, n = 0, len(s)
        
        while l < n:
            while l < n and s[l] ==' ':
                l += 1
                
            if l >= n:
                break
                
            j = l + 1    
            while j < n and s[j] !=' ':
                j += 1
                
            word = s[l:j]
            if len(res) == 0:
                res = word
            else:
                res = word  + ' ' + res
            l = j + 1
            
        return res
            