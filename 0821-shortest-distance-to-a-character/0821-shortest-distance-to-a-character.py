class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        prev = float('-inf')
        ans = []
        
        for idx,char in enumerate(s):
            if char == c:
                prev = idx
            ans.append(idx - prev)
            
        prev = float("inf")
        for i in range(len(s) - 1, -1, -1):
            if s[i] == c:
                prev = i
            ans[i] = min(ans[i], prev - i)
            
        return ans
            
            
        
        